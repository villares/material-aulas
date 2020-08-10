## Desenhando fora da vista (*offscreen buffer*)

É possível desenhar em um objeto especial, uma espécie de tela virtual, criando superfícies *PGraphics* com a função [createGraphics()](https://py.processing.org/reference/createGraphics.html), em vez de desenhar diretamente na tela em uma estratégia conhecida como _offscreen buffer_. Depois é possível mostrar ou não essa imagem na área de desenho normal com a função `image()` (a mesma que usamos para mostrar uma imagem externa carregada carregada com `loadImage()`, uma *PImage*).

**Atenção:** Não esqueça de usar `.beginDraw()` e `.endDraw()` ou você será brindado com uma `NullPointerExeption`

Algumas vantagens dessa estratégia podem ser:
- Desenho cumulativo em uma camada enquanto se anima elementos (com limpeza do frame) em outra camada;
- Potencialmente mais rápido do que desenhar na tela (reaproveitando um desenho com partes já prontas, por exemplo);
- Salvar o desenho em camadas separadas para posterior tratamento (como no exemplo mais abaixo).

```python
def setup():
    size(600, 400)
    
def draw():
    global c0, c1
    # camada 0
    c0 = createGraphics(600, 400)
    c0.beginDraw()
    # c0.background(200) # fundo (opaco)
    c0.clear() # limpa os pixels, deixa transparente
    c0.fill(255, 0, 0)
    c0.rect(100, 100, 100, 100)
    c0.endDraw()
    # camada 1
    c1 = createGraphics(600, 400)
    c1.beginDraw()
    c1.clear() # limpa os pixels, deixa transparente
    c1.fill(0, 0, 200)
    c1.ellipse(200, 200, 200, 200)
    c1.endDraw()
    # desenhe as camandas na tela
    image(c0, 0, 0)
    image(c1, 0, 0)
                    
def keyPressed():
    if key == 's':
        c0.save('camada0.png')
        c1.save('camada1.png')
        saveFrame("camadas-combinadas.png")
```
![camada0](https://user-images.githubusercontent.com/3694604/70395381-dc6f4280-19dc-11ea-8f64-fad20e2c0993.png)
![camada1](https://user-images.githubusercontent.com/3694604/70395382-dc6f4280-19dc-11ea-9d9b-d8a371a1c7d8.png)
![combinadas](https://user-images.githubusercontent.com/3694604/70395383-dd07d900-19dc-11ea-9671-4cf6eb2d510e.png)
