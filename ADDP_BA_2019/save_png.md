# Como exportar uma imagem PNG

O código abaixo exemplifica como salvar uma imagem PNG de um frame. Quando uma tecla é pressionada, é executada a função `keyPressed()` e se for identificada a tecla "s" (`key == 's'`) é execuatada a função `saveFrame()`, que grava uma imagem na pasta do *sketch*.

```python
def setup(): #cria o setup do desenho, inclusive a área da imagem
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)
    
def draw(): #define o plano de fundo e o desenho
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
          
def galho(tamanho): #definição do galho
    ang = radians(mouseX)
    reducao = .8
    strokeWeight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(ang)
        # stroke(255, 0, 0)
        galho(tamanho * reducao - random(0, 2))
        # rotate(-ang * 2)
        rotate(-ang)
        rotate(-ang)
        # stroke(0, 0, 255)
        galho(tamanho * reducao - random(0, 2))
        popMatrix()
          
def keyPressed(): # executada quando uma tecla for precinada
    if keyCode == LEFT:
         seed = seed - 1
    if keyCode == RIGHT:
         seed = seed + 1
    if key == ' ':  # barra de espaço precionada, sorteia nova "seed"
        seed = int(random(100000))
        print(seed)
    if key == 's':  # tecla "s" precionada, salva a imagem PNG
        nome_arquivo = 'arvore-s{}-a{}.png'.format(seed, mouseX % 360)
        saveFrame(nome_arquivo)
        print("Salvando PNG")
```
