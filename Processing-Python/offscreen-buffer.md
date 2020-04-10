## Desenhando fora da vista (*offscreen buffer*)

Aqui um exemplo de desenho feito em superfícies PGraphics (https://py.processing.org/reference/createGraphics.html) em vez de diretamente na tela (uma estratégia conhecida como _offscreen buffer).

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
    global sinalizador
    if key == 's':
        c0.save('camada0.png')
        c1.save('camada1.png')
        saveFrame("camadas-combinadas.png")
```
![camada0](https://user-images.githubusercontent.com/3694604/70395381-dc6f4280-19dc-11ea-8f64-fad20e2c0993.png)
![camada1](https://user-images.githubusercontent.com/3694604/70395382-dc6f4280-19dc-11ea-9d9b-d8a371a1c7d8.png)
![combinadas](https://user-images.githubusercontent.com/3694604/70395383-dd07d900-19dc-11ea-9671-4cf6eb2d510e.png)
