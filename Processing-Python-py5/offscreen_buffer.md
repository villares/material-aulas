# Desenhando em um espaço fora da tela (*offscreen buffer*)

É possível desenhar em um objeto especial, uma espécie de tela virtual, criando superfícies *Py5Graphics* com a função [create_graphics()](https://py5coding.org/reference/sketch_create_graphics.html), em vez de desenhar diretamente na tela em uma estratégia conhecida como _offscreen buffer_. Depois é possível mostrar ou não essa imagem na área de desenho normal com a função `image()`, a mesma que usamos para mostrar uma imagem externa carregada carregada com `load_image()`, um objeto *Py5Image*.

Uma vez instanciada a superfície de desenho com, por exempo, `b = create_graphics(width, height)`, antes de se desenhar é necessário chamar o método `b.begin_draw()`. As instruções de desenho são também invocadas como métodos da superfíe, como por exemplo, `b.backround(0)` ou `b.rect(100, 100, 100, 100)`, e ao final é recomendável encerrar com `b.end_draw()`.

Algumas vantagens dessa estratégia podem ser:

- Desenho cumulativo em uma camada enquanto se anima elementos(com limpeza do frame) em outra camada
- Potencialmente mais rápido do que desenhar na tela (reaproveitando um desenho com partes já prontas, por exemplo)
- Salvar o imagens em camadas separadas para posterior tratamento.
- Aplicação de máscaras de recorte ou outros efeitos

Outra estratégia semelhante é desenhar em um objeto ou *grupo* de objetos *Py5Shape*, que pode ser criado com a função [create_shape()](http://py5coding.org/reference/sketch_create_shape.html), e pode depois desenhado na tela com `shape()'.

## Um primeiro exemplo

```python
def setup():
    size(400, 400)
    global img
    img = create_graphics(400, 400)
    img.begin_draw()
    img.clear()  # limpa os pixels, deixa transparente
    # img.background(200) # fundo (opaco)
    img.fill(255, 0, 0)
    img.rect(100, 100, 100, 100)
    img.end_draw()


def draw():
    background(sin(radians(frame_count * 0.5)) * 128 + 128)
    image(img, 0, 0)
    fill(0, 0, 200)
    circle(mouse_x, mouse_y, 100)
```

## Camadas que podem ser salvas em separado

```python
def setup():
    global c0, c1
    size(600, 400)
    # camada 0
    c0 = create_graphics(600, 400)
    c0.begin_draw()
    # c0.background(200) # fundo (opaco)
    c0.clear()  # limpa os pixels, deixa transparente
    c0.fill(255, 0, 0)
    c0.rect(100, 100, 100, 100)
    c0.end_draw()
    # camada 1
    c1 = create_graphics(600, 400)
    c1.begin_draw()
    c1.clear()  # limpa os pixels, deixa transparente
    c1.fill(0, 0, 200)
    c1.ellipse(200, 200, 200, 200)
    c1.end_draw()

def draw():
    # desenhe as camandas na tela
    image(c0, 0, 0)
    image(c1, 0, 0)

def key_pressed():
    if key == 's':
        c0.save('camada0.png', drop_alpha=False)
        c1.save('camada1.png', drop_alpha=False)
        save_frame("camadas-combinadas.png")
```

![camada0](https://user-images.githubusercontent.com/3694604/70395381-dc6f4280-19dc-11ea-8f64-fad20e2c0993.png)
![camada1](https://user-images.githubusercontent.com/3694604/70395382-dc6f4280-19dc-11ea-9d9b-d8a371a1c7d8.png)
![combinadas](https://user-images.githubusercontent.com/3694604/70395383-dd07d900-19dc-11ea-9671-4cf6eb2d510e.png)

# 
