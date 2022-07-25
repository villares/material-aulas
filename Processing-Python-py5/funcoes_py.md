# Definindo e chamando funções

>[**função**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:função)
> uma sequência nomeada de declarações que executa alguma operação útil. as funções podem receber argumentos ou não e podem ou não produzir algum resultado.

ao programar podemos inventar vocabulário novo na linguagem que estamos usando quando definimos uma função. essa palavra se comporta exatamente como outras palavras que já vem prontas na linguagem, e * encapsula*, empacota, alguma ação útil, por meio de um trecho de código, o corpo da função, que é executado quando * chamamos * a função em um outro momento.

leia com cuidado estes três exemplos, escritos de maneira genérica, com nomes bobos(`nome_da_funcao`, `outra_funcao`, `funcao_com_resultado`) mas que exemplificam a estrutura da definição de uma nova função. onde está `corpo` entram indentadas em relação ao cabeçalho(a linha do `def`), as ações que a função executa.

# Sintaxe para definição de funções
```python
def nome_da_funcao(a, b):  # esta função tem dois parâmetros: a e b (requer dois argumentos)
     corpo  # instruções que a função executa, usando valores dos parâmetros

def outra_funcao():  # esta função não tem nenhum parâmetro (não requer argumentos na chamada)
     corpo  # instruções que a função executa

def funcao_com_resultado(a):  # esta função tem um parâmetro
     parte_do_corpo    # instruções que calculam um valor/resultado
     return resultado  # esta linha também pertence ao corpo da função

# Podemos também ter funções que não requerem argumentos (não tem
# parâmetros) e devolve resultado.
```


# Sintaxe da invocação, ou chamada, de funções

vamos ver agora como seria o uso dessas novas palavras, comparando com palavras da linguagem que já vimos antes.

```python
nome_da_funcao(valor, outro_valor)  # esta função precisa de dois argumentos
# um exemplo que já vimos
fill(255, 100)  # pede preenchimento branco tranlúcido

outra_funcao()  # esta função não requer argumentos
# um exemplo de função que não tem parâmetros visto anteriormente
no_fill()  # desliga o preenchimento das formas a ser desenhadas

# O resultado de uma função pode ser usado em uma atribuição, ou dentro de
# outra estrutura
a=funcao_com_resultado(valor)
print(funcao_com_resultado(valor))
# um exemplo de função que devolve resultado visto anteriormente
r=random(256)
# a função inteira usada como argumento de outra função!
fill(random(256), random(256), random(256))
```

os parâmetros, quando existem, são nomes lá dentro da definição da função, que recebem os valores dos argumentos usados quando a função é chamada.

# Exemplo da função `olho()`

```python
def setup():
    size(400, 400)
    background(0)  # cor do fundo
    # chamando a função olho várias vezes
    olho(300, 100, 100)  # x, y, tamanho
    olho(100, 200, 50)
    tamanho_sorteado=random(10, 150)
    olho(200, 300, tamanho_sorteado)

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

as funções que são feitas para devolver um resultado contém a palavra `return` no seu corpo, seguida do resultado calculado. A instrução `return` pode aparecer no meio da função, mas sempre que for executada interrompe a execucão da função, *devolvendo * o fluxo de execução para o ponto onde a função foi chamada.

< sup > se não houver um valor depois de `return` no corpo, a função devolve o valor especial `None`, o mesmo que acontece com funções que não tem `return`, só que no ponto onde está escrito `return`. < /sup >

aqui alguns exemplos:

```python
def cor_sorteada():
    """Sorteia uma cor RGB"""
    r=random(256)
    g=random(256)
    b=random(256)
    cor=color(r, g, b)
    return cor  # instrução que devolve a cor e retorna o fluxo de execução
```

(função do exemplo anterior em uso)

```python
fill(cor_sorteada())   # pede um preenchimento com uma cor sorteada!
rect(10, 10, 100, 50)
```

da mesma maneira todo o tipo de manipulação de valores pode ser encapsulada em uma função.

```python
def media(a, b):
     return (a + b) / 2.

print(media(100, 21))
# resultado: 60.5
```

mais um exemplo

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

# Glossário

[**encapsulamento**](https: // penseallen.github.io/pense_python2e/04-caso-interface.html  # termo:encapsulamento) O processo de transformar uma sequência de instruções em uma definição de função.

[**definição de função**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:definição%20de%20função) Uma instrução que cria uma função nova, especificando seu nome, parâmetros e as instruções que contém.

[**cabeçalho**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:cabeçalho) A primeira linha de uma definição de função.

[**corpo**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:corpo) A sequência de instruções dentro de uma definição de função.

[**parâmetro**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:parâmetro) Um nome usado dentro de uma função para se referir ao valor passado como argumento.

[**chamada de função**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:chamada%20de%20função) Uma instrução que executa uma função. É composta pelo nome da função seguido de uma lista de argumentos entre parênteses, ou caso a função possa ser chamada sem argumentos, só os parênteses (`nome()`).

[**argumento**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:argumento) Um valor apresentado a uma função quando a função é chamada. Este valor é atribuído ao parâmetro correspondente na função.

[**valor de retorno**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:valor%20de%20retorno) O resultado de uma função. Se uma chamada de função for usada como uma expressão, o valor de retorno é o valor da expressão.

[**função com resultado**](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:função%20com%20resultado) Uma função que devolve um valor.

[**`None`** ](https: // penseallen.github.io/pense_python2e/03-funcoes.html  # termo:None) Um valor especial apresentado por funções nulas (circularmente definidas como funções que devolvem o valor `None`, em lugar de outro valor de resultado).

# Assuntos relacionados

- [parâmetros opcionais e outras malandragens](funcoes_2.md)
- [recursividade em funções](recursao_py.md)

- --
texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
