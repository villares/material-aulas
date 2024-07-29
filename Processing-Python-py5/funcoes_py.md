# Definindo e chamando funções

>[**função**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:função)
> Uma sequência nomeada de declarações que executa alguma operação útil. As funções podem receber argumentos ou não e podem ou não produzir algum resultado.

Ao programar podemos inventar vocabulário novo na linguagem que estamos usando quando definimos uma função. Essa palavra se comporta exatamente como outras palavras que já vem prontas na linguagem, e *encapsula*, empacota, alguma ação útil, por meio de um trecho de código, o corpo da função, que é executado quando *chamamos* a função em um outro momento.

Leia com cuidado estes três exemplos, escritos de maneira genérica, com nomes bobos (`nome_da_funcao`, `outra_funcao`, `funcao_com_resultado`) mas que exemplificam a estrutura da definição de uma nova função. Onde está `corpo` entram indentadas em relação ao cabeçalho (a linha do `def`), as ações que a função executa.

## Sintaxe para definição de funções

```python
def nome_da_funcao(a, b):  # esta função tem dois parâmetros: a e b (requer dois argumentos)
     corpo  # instruções que a função executa, usando valores dos parâmetros

def outra_funcao():  # esta função não tem nenhum parâmetro (não requer argumentos na chamada)
     corpo  # instruções que a função executa

def funcao_com_resultado(a):  # esta função tem um parâmetro
     parte_do_corpo    # instruções que calculam um valor/resultado
     return resultado  # esta linha também pertence ao corpo da função

# Podemos também ter funções que não requerem argumentos (não tem parâmetros) e devolve resultado.
```

## Sintaxe da invocação, ou chamada, de funções

Vamos ver agora como seria o uso dessas novas palavras, comparando com palavras da linguagem que já vimos antes.

```python
nome_da_funcao(valor, outro_valor)  # esta função precisa de dois argumentos
# um exemplo que já vimos
fill(255, 100)  # pede preenchimento branco tranlúcido

outra_funcao()  # esta função não requer argumentos
# um exemplo de função que não tem parâmetros visto anteriormente
no_fill()  # desliga o preenchimento das formas a ser desenhadas

# O resultado de uma função pode ser usado em uma atribuição, ou dentro de
# outra estrutura
a = funcao_com_resultado(valor)
print(funcao_com_resultado(valor))

# um exemplo de função que devolve resultado visto anteriormente
r = random(256)
# a função inteira usada como argumento de outra função!
fill(random(256), random(256), random(256))
```

Os parâmetros, quando existem, são nomes lá dentro da definição da função, que recebem os valores dos argumentos usados quando a função é chamada.

## Um exemplo de função, uma função `olho()`

![olho](assets/funcao_olho.png)

```python
def setup():
    size(400, 400)
    background(0)  # cor do fundo
    # chamando a função olho várias vezes
    olho(300, 100, 100)  # x, y, tamanho
    olho(100, 200, 50)
    olho(200, 300, 75)

# definindo a função olho
def olho(x, y, tamanho):
    """Olho precisa de 3 parâmetros, x e y para posição, e tamanho"""
    no_stroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho / 2)
    fill(0)
    circle(x, y, tamanho * 0.40)
```

# Funções que devolvem resultados

A função `olho()` desenha um olho mas não devolve nenhum valor, na verdade ela devolve o valor especial `None` (uma espécie de "nada"), mas é comum termos funções que devolvem algum valor útil como resultado.

As funções que são feitas para devolver um resultado contém a palavra `return` no seu corpo, seguida do resultado calculado. A instrução `return` pode aparecer no meio da função, mas sempre que for executada interrompe a execucão da função, *devolvendo* o fluxo de execução para o ponto onde a função foi chamada.

<sup>Se não houver uma expressão ou valor depois na palavra chave `return` em uma linha do corpo da função, esta se encerrará caso a linha seja executada e será devolvido o valor especial `None`, o mesmo valor que é devolvido por funções que não tem `return` no corpo quando chegam ao final e se encerram.</sup>

Aqui alguns exemplos:

```python
def cor_sorteada():
    """Sorteia uma cor RGB"""
    r = random(256)
    g = random(256)
    b = random(256)
    cor = color(r, g, b)
    return cor  # instrução que devolve a cor e retorna o fluxo de execução
```

(função do exemplo anterior em uso)

```python
fill(cor_sorteada())   # pede um preenchimento com uma cor sorteada!
rect(10, 10, 100, 50)
```

Da mesma maneira todo o tipo de manipulação de valores pode ser encapsulada em uma função.

```python
def media(a, b):
     return (a + b) / 2.

print(media(100, 21))
# resultado: 60.5
```

Mais um exemplo

```python
def menor_de_idade(idade):
     if idade < 18:
          return True
     else:
          return False

# Poderia ser escrito abreviadamente assim...
# def menor_de_idade(idade):
#     return idade < 18
```

(função do exemplo anterior em uso)

```python
if menor_de_idade(idade_aluno):
     print('quer um refri?')
else:
     print('quer uma cerveja?')
```

## Alerta: Mágica escondida!

Para que uma função seja executada pelo Python, ela precisa ser "chamada", também dizemos "invocada", por meio de seu nome e os parênteses justapostos. Mas se você olhar atentamente, onde estão as chamadas para `setup()` e `draw()`?

A biblioteca py5 faz essas chamadas para nós dentro da função `run_sketch()`, que por sua vez está sendo chamada automaticamente 
para pelo *plug-in* `thonny-py5mode`, quando a opção *imported mode for py5* está ligada, no Thonny IDE. A função `run_sketch()` cuida então de chamar para nós a função `setup()` logo no ínicio apenas uma vez, e `draw()` sem parar, no que é conhecido às vezes como "laço principal de animação" do sketch. Da mesma forma, as "funções de evento", como `key_pressed()`, e outras tantas, são chamadas pela biblioteca.

> Mais detalhes ainda (se você tiver curiosidade): Isso tudo foi feito para simplificar a experiência de quem está programando. Além chamar as funções apropriadas, o plug-in também evita que tenhamos que digitar `py5.` como prefixo em todas as funções que vem da biblioteca. Então isso tudo é um pouco mágico e pode parecer um pouco confuso.
> As coisas acontecem de maneira um pouco mais explícita quando usamos o chamado *module mode*, que é o estilo que tem `import py5` no começo do código e termina em geral justamente com `py5.run_sketch()`. E nesse caso todas as funções que vem da biblioteca precisam do prefixo `py5.`, e ficam assim:
> ```python
> import py5
> 
> def setup():
>     py5.size(500, 500)
>     py5.background(200, 200, 0)
>     ...
> py5.run_sketch()  # aqui dentro py5 vai chamar, setup(), draw() e as funções de evento
> ```
> Mas tem ainda outras malandragens ocultas que a biblioteca faz, mesmo no *module mode*, como desmembrar a função `setup()` em `setup()` e `settings()` para nos facilitar a vida!

## Abstração

Você vai ouvir pessoas falando sobre as ideias de abstração e encapsulamento na programação, alguns autores associam em especial o termo encapsulamento às ideias de orientação a objetos, mas o autor Allen Downey, por exemplo, o usa também no contexo da criação de funções.

Ambas as palavras remetem ao poder de se dar nomes a reunião de elementos que capturam, de alguma forma, a essencia do que esses elementos reunidos fazem, escondendo detalhes do seu funcionamento conjunto. Isso é o que fazemos ao criar e nomear funções. Posteriormente podemos compor abstrações ainda maiores usando as funções que criamos anteriormente, e no caso da orientação a objetos nomear classes cujos objetos tem suas próprias funções, os métodos.

## Glossário

[**encapsulamento**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:encapsulamento) O processo de transformar uma sequência de instruções em uma definição de função.

[**definição de função**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:definição%20de%20função) Uma instrução que cria uma função nova, especificando seu nome, parâmetros e as instruções que contém.

[**cabeçalho**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:cabeçalho) A primeira linha de uma definição de função.

[**corpo**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:corpo) A sequência de instruções dentro de uma definição de função.

[**parâmetro**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:parâmetro) Um nome usado dentro de uma função para se referir ao valor passado como argumento.

[**chamada de função**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:chamada%20de%20função) Uma instrução que executa uma função. É composta pelo nome da função seguido de uma lista de argumentos entre parênteses, ou caso a função possa ser chamada sem argumentos, só os parênteses (`nome()`).

[**argumento**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:argumento) Um valor apresentado a uma função quando a função é chamada. Este valor é atribuído ao parâmetro correspondente na função.

[**valor de retorno**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:valor%20de%20retorno) O resultado de uma função. Se uma chamada de função for usada como uma expressão, o valor de retorno é o valor da expressão.

[**função com resultado**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:função%20com%20resultado) Uma função que devolve um valor.

[**`None`** ](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:None) Um valor especial apresentado por funções nulas (circularmente definidas como funções que devolvem o valor `None`, em lugar de outro valor de resultado).

# Assuntos relacionados

- [Parâmetros opcionais e outras malandragens](funcoes_2.md)
- [Recursividade em funções](recursao_py.md)

---

Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
