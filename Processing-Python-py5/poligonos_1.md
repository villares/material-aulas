# Desenhando polígonos - I

## Primeiro contato

Processing oferece funções para desenhar triângulos `triangle()` e quadriláteros `quad()` que são chamadas usando 3 e 4 pares de números, as coordenadas para 3 e 4 vértices, respectivamente. Veja o exemplo a seguir:

![triângulo e quadrilátero](https://user-images.githubusercontent.com/3694604/188685363-824deb7a-8af9-4e4b-928e-4a84380ef69c.png)

Mas e se quisermos desenhar um polígono com 5, 6 ou com um número arbitrário de vértices?

Neste caso usamos um conjuto de funções!

Tudo começa com `begin_shape()`, seguido da repetição da função `vertex()` para cada vértice, terminando com `end_shape()`. Quando usado com a constante `CLOSE`, `end_shape(CLOSE)`, produz polígonos fechados.

```python
size(400, 200)

begin_shape()  # inicia o polígono da esquerda
vertex(10, 10)
vertex(50, 50)
vertex(190, 30)
vertex(90, 150)
vertex(30, 100)
end_shape()  # polígono aberto

begin_shape()  # inicia o polígono da direita
vertex(210, 10)
vertex(250, 50)
vertex(390, 30)
vertex(290, 150)
vertex(230, 100)
end_shape(CLOSE)  # polígono fechado
```
![e4](assets/beginShape_endShape.png)

## Uma forma alternativa

O Python tem uma estratégia expecial que é aproveitada por quem prepara as bibliotecas para nós quando é preciso "começar" e "encerrar" uma operação depois de um certo ponto do programa, como no exemplo acima o `begin_shape()` e `end_shape()`. Essa essa estratégia propõe que você comece um "contexto" em que a operação está acontecendo com a palavra chave `with` e uma chamda para uma função que cria um *gerenciador de contexto*. Então você indica pela indentação do código as coisas que precisam acontecer naquele contexto, por exemplo enquanto o o `begin_shape()` está em ação. Quando a indentação acaba, o contexto se encerra, e o *gerenciador de contexto* cuida de encerrar o que tiver que ser encerrado. Veja como é possível desenhar os mesmos polígonos anteriores com essa estratégia.

```python
size(400, 200)

with begin_shape():  # inicia o polígono aberto
    vertex(10, 10)
    vertex(50, 50)
    vertex(190, 30)
    vertex(90, 150)
    vertex(30, 100)
# acaba a indentação e terminou o desenho do polígono

with begin_closed_shape():  # inicia o polígono fechado
    vertex(210, 10)
    vertex(250, 50)
    vertex(390, 30)
    vertex(290, 150)
    vertex(230, 100)
# aqui já acabou o desenho do polígono
```

## Desenhando uma estrela de quatro pontas

Vejamos um exemplo que combina a estrutura que vimos antes com o uso de variáveis para calcular a posição dos vértices, formando um estrela!

```pyde
size(400, 400)
background(0, 0, 200)  # um fundo azul
x, y = width / 2, height / 2  # coordenadas do centro

largura_total, largura_menor = 250, 150
a = largura_total / 2
b = largura_menor / 2

with begin_closed_shape():
    vertex(x - a, y - a)
    vertex(x - b, y)
    vertex(x - a, y + a)
    vertex(x, y + b)
    vertex(x + a, y + a)
    vertex(x + b, y)
    vertex(x + a, y - a)
    vertex(x, y - b)
```

![e4](assets/estrela_4_pontas.png)

# Assuntos relacionados

- Animando uma estrela com[`setup()`, `draw()` e o movimento do mouse](indentacao.md).
- Usos mais avançados de `begin_shape()` na[referência](https://py.processing.org/reference/begin_shape.html).
- [Criando os vértices a partir de estruturas de dados com laços de repetição e como fazer polígonos com furos](poligonos_2.md).
- Crie estrelas de muitas pontas usando[laços de repetição `while`](while.md).
