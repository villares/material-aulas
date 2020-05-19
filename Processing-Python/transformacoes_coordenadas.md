# Transformando o sistema de coordenandas

> Baseado no tutorial [py.processing.org/tutorials/transform2d/](https://py.processing.org/tutorials/transform2d/) de J. David Eisenberg

[Baixe os arquivos deste tutorial](https://py.processing.org/tutorials/transform2d/imgs/transform2d.zip)

Processing tem funções embutidas que tornam fácil você mover, girar, ecrescer ou encolher objetos em um *sketch*. Este tutorial vai apresentar você às funções `translate`, `rotate`, e `scale`. De maneira que você as possa usar nos seus *sketches*.

### Translação: Movendo a grade

Como você sabe, sua janela do Processing funciona como um pedaço de papel milimetrado. Quando você quer desenhar alguma coisa, especifica as cordenadas. Veja um retângulo simples desenhado com o código `rect(20, 20, 40, 40)`. O sistema de coordenadas (um nome sofisticado para o nosso "papel milimetrado") está mostrado em cinza.

![Black rectangle on gray numbered grid](https://py.processing.org/tutorials/transform2d/imgs/original.png)

Se você quiser mover o retângulo 60 unidades para a direita e 80 unidades para baixo, pode mudar as coordenadas somando ao *x* e *y* do ponto inicial: `rect(20 + 60, 20 + 80, 40, 40)` e o retângulo vai aparecer em um local diferente. (Pusemos a seta aí para efeito dramático.)

![Black rectangle on gray numbered grid, moved](https://py.processing.org/tutorials/transform2d/imgs/new_coords.png)

Mas tem uma maneira mais interessante de fazer isso: **em vez disso mover o papel milimetrado**. Se você moveo o papel milimetrado 60 unidades para a direita e 80 para baixo vai obter exatamente o mesmo resultado visual. Mover o sistema de coordenadas é chamado de translação.

![grid moved with arrow showing motion](https://py.processing.org/tutorials/transform2d/imgs/moved_grid.png)

A coisa importante de se notar no diagrama anterior é que, do ponto de vista do retângulo, ele não se moveu nada. O canto superior esquerdo continual em (20,20). Quando você usa transformações, as coisas que você desenha *nunca* mudam de posição; o sistema de cordenadas muda.

Abaixo o código que desenha o retângulo em vermelho mudando suas coordenadas, e então desenha em azul movendo a grade. Os retângulos são translúcidos de maneira que você pode ver que estão (visualmente) no mesmo lugar. Apenas o método usado para movê-los mudou. Copie este código no Processing e experimente:

```python
def setup():
    size(200, 200)
    background(255)
    noStroke()

    # draw the original position in gray
    fill(192)
    rect(20, 20, 40, 40)
    
    # draw a translucent red rectangle by changing the coordinates
    fill(255, 0, 0, 128)
    rect(20 + 60, 20 + 80, 40, 40)
        
    # draw a translucent blue rectangle by translating the grid
    fill(0, 0, 255, 128)
    pushMatrix()
    translate(60, 80)
    rect(20, 20, 40, 40)
    popMatrix()
```

Vamos olhar o código de conversão em mais detalhes.`pushMatrix()` é uma função embutida que salva a posição atual do sistema de coordendas. O `translate(60, 80)` movbaixo. O `rect(20, 20, 40, 40)` desenha o retângulo no mesmo local em que estava originalmente. Lembre-se de que as coisas que você desenha não se movem - a grade se move. Por fim,`popMatrix()` restaura o sistema de coordenadas como estava antes de você fazer a translação.

Sim, você podia ter feito uma translação `translate(-60, -80)` para mover a grade de volta a sua posição original. No entanto, quando você começa a executar operações mais sofisticadas com o sistema de coordenadas, é mais fácil usar `pushMatrix()` e `popMatrix()` para salvar e restaurar o status em vez de precisar desfazer todas as suas operações. Mais adiante neste tutorial, você descobrirá por que essas funções parecem ter nomes tão estranhos.

### Qual é a vantagem?

Você pode estar pensando que pegar o sistema de coordenadas e movê-lo é muito mais complicado do que apenas adicionar às coordenadas. Para um exemplo simples, como o retângulo, você está correto. Mas vamos dar um exemplo de onde o `translate()` pode facilitar a vida. Aqui está um código que desenha uma fileira de casas. Ele usa um loop que chama a função chamada `casa()`, que recebe o *x* e *y* da posição do canto superioe esquerdo da casa como parâmetros.

![Row of stick-figure casas](https://py.processing.org/tutorials/transform2d/imgs/houses.png)

```python
def setup():
    size(400, 100)
    background(255)
    for i in xrange(10,350,50):
        casa(i, 20)

```

Este é o código para desenhar a casa alterando sua posição. Veja todos os acréscimos que você precisa acompanhar.

```python
def casa(int x, int y):
    triangle(x + 15, y, x, y + 15, x + 30, y + 15)
    rect(x, y + 15, 30, 30)
    rect(x + 12, y + 30, 10, 15)
```

Compare isso com a versão da função que usa `translate()`. Neste caso o código desenha a casa no mesmo lugar, com o canto superior esquerdo em (0, 0), e deixa a translação fazer todo o trabalho.

```python
def casa(int x, int y):
    pushMatrix()
    translate(x, y)
    triangle(15, 0, 0, 15, 30, 15)
    rect(0, 15, 30, 30)
    rect(12, 30, 10, 15)
    popMatrix()
```

### Rotação

Além da translação, que move a grade, é possível girar o sistema de coordenadas com a função `rotate()`. Essa função tem um parâmetro ou argumento, um número de *radianos* que você quer rodar. Em graus, um círculo tem 360°. Quando descrevemos os ângulos em radianos, a circuferência completa tem 2π radianos. Eis aqui um diagrama de como Processing mede ângulos em graus (preto) e radianos (vermelho).

![Degrees are measured clockwise with zero being at 3 o'clock](https://py.processing.org/tutorials/transform2d/imgs/degrees.png)

Como a maioria das pessoas pensa em graus, o Processing possui uma função embutida `radians()` que recebe um número em graus como argumento e o converte para você. Ele também possui uma função    `degrees()` que converte radianos em graus. Dado esse cenário, vamos tentar girar um quadrado 45 graus no sentido horário.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    fill(192)
    noStroke()
    rect(40, 40, 40, 40)
    
    pushMatrix()
    rotate(radians(45))
    fill(0)
    rect(40, 40, 40, 40)
    popMatrix()
```
Ei o que aconteceu? Como o quadrado foi movido e cortadao A resposta é: o quadrado não se moveu. A **grade** foi girada. Aqui está o que realmente aconteceu. Como você pode ver, no sistema de coordenadas girado, o quadrado ainda tem seu canto superior esquerdo em (40, 40).

![shows grid rotated 45 degrees clockwise](https://py.processing.org/tutorials/transform2d/imgs/rotated_grid.png)

### Girando da maneira certa

A maneira certa de girar o quadrado é:

1. Faça a translação da origem do sistema de coordenadas (0, 0) para onde você quer que seja o canto superior esquerdo do quadrado.
2. Gire a grade π/4 radianos (45°)
3. Desenhe o quadrado na origem.

![Grid translated, then rotated](https://py.processing.org/tutorials/transform2d/imgs/correct_rotate_grid.png)

E aqui está o código que gera o resultado, sem as marcas de grade.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    fill(192)
    noStroke()
    rect(40, 40, 40, 40)
        
    pushMatrix()
    # mova a origem para o ponto de giro
    translate(40, 40)
        
    # em seguida gire a grade
    rotate(radians(45))
        
    # e desenhe o quadrado na origem
    fill(0)
    rect(0, 0, 40, 40)
    popMatrix()
```

E aqui está um programa que gera uma roda de cores usando rotação. A captura de tela é reduzida para economizar espaço.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    noStroke()

def draw():
    if (frameCount % 10 == 0):
        fill(frameCount * 3 % 255,
             frameCount * 5 % 255,
             frameCount * 7 % 255)
        pushMatrix()
        translate(100, 100)
        rotate(radians(frameCount * 2    % 360))
        rect(0, 0, 80, 20)
        popMatrix()
```

### Escalando

A transformação final do sistema de coordenadas é a mudança de escala, que altera o tamanho da grade. Dê uma olhada neste exemplo, que desenha um quadrado, depois redimensiona a grade para o dobro do tamanho normal e a desenha novamente.

```python
def setup():
    size(200,200)
    background(255)
        
    stroke(128)
    rect(20, 20, 40, 40)
        
    stroke(0)
    pushMatrix()
    scale(2.0)
    rect(20, 20, 40, 40)
    popMatrix()
```
Primeiro, você pode ver que o quadrado parece ter se movido. Claro que não. Seu canto superior esquerdo ainda está em (20, 20) na grade escalada para cima, mas esse ponto está agora duas vezes mais distante da origem do que no sistema de coordenadas original. Você também pode ver que as linhas são mais grossas. Isso não é ilusão de ótica - as linhas realmente têm o dobro da espessura, porque o sistema de coordenadas foi dimensionado para dobrar seu tamanho.

> **Desafio de programação** aumente a o tamnaho do quadrado preto, mas mantenha o cantto superior esquerdo dele no mesmo lugar do quadrado cinza. Dica: use `translate()` para mover a origem, então use `scale()`.

Não tem um lei que diz que você tem que escalar as dimensões em *x* e *y* igualmente. Tente usar `scale(3.0, 0.5)` para fazer a dimensão em    *x* três vezes maior e a dimensão em *y* metado do tamanho normal.

### A ordem importa

Quando você faz várias transformações, a ordem faz diferença. Uma rotação seguida de uma translação seguida por uma mudança de escala não produzirá os mesmos resultados que uma translação seguida de uma rotação e uma mudança de escala. Aqui está um exemplo de código e os resultados.

```python
def setup():
    size(200, 200)
    background(255)
    smooth()
    line(0, 0, 200, 0)    # desenha eixos
    line(0, 0, 0, 200)
        
    pushMatrix()
    fill(255, 0, 0)    # quadrado vermelho
    rotate(radians(30))
    translate(70, 70)
    scale(2.0)
    rect(0, 0, 20, 20)
    popMatrix()

    pushMatrix()
    fill(255)    # quadrado branco
    translate(70, 70)
    rotate(radians(30))
    scale(2.0)
    rect(0, 0, 20, 20)
    popMatrix()
```

### A matriz de transformação

Sempre que você faz uma rotação, translação ou mudança de escla, as informações necessárias para a transformação são acumuladas em uma tabela de números. Essa tabela, ou matriz, possui apenas algumas linhas e colunas; no entanto, através do milagre da matemática, ela contém todas as informações necessárias para realizar qualquer série de transformações. E é por isso que `pushMatrix ()` e `popMatrix ()` têm essa palavra em seu nome.

### Push e Pop

Sobre a parte *push* e *pop* dos nomes? Elas vêm de um conceito de computação conhecido como pilha, que funciona como um dispensador de bandejas com mola em uma lanchonete. Quando alguém devolve uma bandeja para a pilha, seu peso empurra a plataforma para baixo. Quando alguém precisa de uma bandeja, ela a pega da parte superior da pilha e as bandejas restantes aparecem um pouco.

De maneira semelhante, `pushMatrix()` coloca o status atual do sistema de coordenadas no topo de uma área de memória, e `popMatrix()` pega de volta o status. O exemplo anterior usou `pushMatrix()` e `popMatrix()` para garantir que o sistema de coordenação estivesse "limpo" antes de cada parte do desenho. Em todos os outros exemplos, as chamadas para essas duas funções não eram realmente necessárias, mas não custa nada salvar e restaurar o status da grade.

Nota: Em Processing, o sistema de coordenadas é restaurado ao seu estado original (origem na parte superior esquerda da janela, sem rotação e sem mudança de escala) toda vez que a função `draw()` é executada.

### Transformações Tri-dimensionais

Se você estiver trabalhando em três dimensões, poderá chamar a função `translate()` com três argumentos para as distâncias *x*, *y*, e *z*. Da mesma forma, você vhama `scale()` com três argumentos que indicam o quanto você deseja que a grade seja redimensionada em cada uma dessas dimensões

Para rotação, chame as funções `rotateX()`, `rotateY()`, ou `rotateZ()` para girar em torno de cada um dos eixos. Todas essas três funções esperam um argumento: o número de radianos a serem rotacionados.
