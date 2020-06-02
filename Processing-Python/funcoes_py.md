# Definindo e chamando funções

>[**função**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:função)
>Uma sequência nomeada de declarações que executa alguma operação útil. As funções podem receber argumentos ou não e podem ou não produzir algum resultado.

### Sintaxe para definição de funções
```python
def nome_da_funcao(a, b): # esta função tem dois parâmetros: a e b (requer dois argumentos)
     corpo  # instruções que a função executa, usando valores dos parâmetros
     
def outra_funcao(): # esta função não tem nenhum parâmetro (não requer argumentos na chamada)
     corpo  # instruçÕes que a função executa

def funcao_com_resultado(a): # esta função tem um parâmetro
     corpo  # instruções que calculam um valor/resultado
     return resultado
     
# Podemos ter funções que não requerem argumentos (não tem parâmetros) e devolve resultado.
```

### Sintaxe da invocação, ou chamada, de funções

```python
nome_da_funcao(valor, outro_valor) # esta função precisa de dois argumentos
# um exemplo que já vimos
fill(255, 100)  # pede preenchimento branco tranlúcido

outra_funcao() # esta função não requer argumentos
# um exemplo de função que não requer parâmetros que já vimos
noFill()  # desliga o preenchimento das formas a ser desenhadas

# O resultado de uma função pode ser usado numa atribuição, ou dentro de outra estrutura
a = funcao_com_resultado(valor)
# um exemplo de função que devolve resultado que já vimos
r = random(256)
fill(random(256), random(256), random(256))
```

Os parâmetros, quando existem, são nomes lá dentro da definição da função, que recebem os valores dos argumentos usados quando a função é chamada.

### Exemplo da função `olho()`

```python
def setup():
    size(400, 400)
    background(0) # cor do fundo 
    # chamando a função olho várias vezes
    olho(300, 100, random(50, 100)) # x, y, tamanho sorteado
    olho(100, 200, random(10, 150)) 
    olho(200, 300, random(10, 150))

# definindo a função olho
def olho(x, y, tamanho):
    """Olho precisa de 3 parâmetros"""
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho/2)
    fill(0)
    circle(x, y, tamanho*.40)
```

### Funções que devolvem resultados

A função `olho()` desenha um olho mas não devolve nenhum valor, na verdade ela devolve o valor especial `None` (uma espécie de "nada"), mas é comum termos funções que devolvem algum valor como resultado.

As funções que são feitas para devolver um resultado contém a palavra `return`, seguida do resultado no seu corpo, e são interrompidas assim que essa instrução é executada. Aqui alguns exemplos:

```python
def cor_sorteada():
    """Sorteia uma cor RGB"""
    r = random(256)
    g = random(256)
    b = random(256)
    cor = color(r, g, b)
    return cor # instrução que devolve a cor e retorna o fluxo de execução
```

Uso:
```python
fill(cor_sorteada())   # pede um preenchimento com uma cor sorteada!
rect(10, 10, 100, 50)
```

Da mesma maneira todo o tipo de manipulação de valores pode ser "encapsulada" em uma função.

```python
def media(a, b):
     return (a + b) / 2.
```

#### Glossário

[**encapsulamento**](https://penseallen.github.io/PensePython2e/04-caso-interface.html#termo:encapsulamento) O processo de transformar uma sequência de instruções em uma definição de função.

[**definição de função**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:definição%20de%20função) Uma instrução que cria uma função nova, especificando seu nome, parâmetros e as instruções que contém.

[**cabeçalho**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:cabeçalho) A primeira linha de uma definição de função.

[**corpo**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:corpo) A sequência de instruções dentro de uma definição de função.

[**parâmetro**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:parâmetro) Um nome usado dentro de uma função para se referir ao valor passado como argumento.

[**chamada de função**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:chamada%20de%20função) Uma instrução que executa uma função. É composta pelo nome da função seguido de uma lista de argumentos entre parênteses, ou caso a função possa ser chamada sem argumentos, só os parênteses (`nome()`).

[**argumento**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:argumento) Um valor apresentado a uma função quando a função é chamada. Este valor é atribuído ao parâmetro correspondente na função.

[**valor de retorno**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:valor%20de%20retorno) O resultado de uma função. Se uma chamada de função for usada como uma expressão, o valor de retorno é o valor da expressão.

[**função com resultado**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:função%20com%20resultado) Uma função que devolve um valor.

[**`None`**](https://penseallen.github.io/PensePython2e/03-funcoes.html#termo:None) Um valor especial apresentado por funções nulas (circularmente definidas como funções que devolvem o valor `None`, em lugar de outro valor de resultado).

## Assuntos relacionados

- Parâmetros padrão [TO DO]
- [Recursividade em funções](recursao_py.md)


---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
