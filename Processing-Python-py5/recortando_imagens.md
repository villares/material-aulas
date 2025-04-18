# Recortando imagens

## Copiando trechos retangulares de uma imagem

## Recortando imagens com uma máscara

```python
def setup():
    global img
    size(500, 500)
    img = load_image('https://garoa.net.br/mediawiki/images/thumb/Convite_NdP_ago.png/750px-Convite_NdP_ago.png')
    # a máscara tem que ter tamanho igual a da imagem que vai ser clipada
    clip_mask = create_graphics(img.width, img.height)
    clip_mask.begin_draw()
    clip_mask.no_fill()
    for i in range(256):
        clip_mask.stroke(255 - i)  # cor de traço vai de branco a preto
        clip_mask.circle(img.width / 2, img.height / 2, i * 2)
    clip_mask.end_draw()
    img.mask(clip_mask)  # esta operação modifica a imagem
    image_mode(CENTER)

def mouse_pressed():
    translate(mouse_x, mouse_y)
    rotate(random(PI))
    image(img, 0, 0)
```

![image](https://user-images.githubusercontent.com/3694604/188531711-8143041d-515d-41ab-ab81-d6d494d0c45c.png)

# Criando uma máscara dinamicamente

![clipping mask](https://user-images.githubusercontent.com/3694604/188624349-0c7e0880-ad0d-47f1-b594-26da4393d459.png)

```python
def setup():
    global offscreen, clip_mask
    size(800, 500)
    # vamos usar uma área de desenho fora da tela "offscreen buffer"
    offscreen = create_graphics(400, height)
    offscreen.begin_draw()  # necessário antes de desenhar na área
    offscreen.background(0, 200, 0)
    offscreen.fill(255)
    for _ in range(100):
        offscreen.rect(random(width / 2), random(height), 50, 50)
    offscreen.end_draw()  # também é preciso encerrar o desenho
    cursor(CROSS)  # cursor em cruz
    clip_mask = create_graphics(int(width / 2), height)

def draw():
    background(150, 150, 200)
    # Uma outra área de desenho que vai ser uma máscara de recorte:  Regiões
    # brancas na máscara indicam posiçoes da imagem final que são mostradas,
    # regiões pretas serão ocultadas e as cinzas intermediárias mostradas
    # translúcidas
    clip_mask.begin_draw()
    clip_mask.clear()
    clip_mask.no_fill()  # usaremos círculos vazados
    for i in range(128):
        clip_mask.stroke(255 - i * 2)  # cor de traço variável
        clip_mask.circle(mouse_x, mouse_y, i)
    clip_mask.end_draw()

    result = offscreen.copy()  # uma cópia da imagem original
    result.mask(clip_mask)     # esta operação modifica a imagem
    image(result, 0, 0)        # mostra a imagem modificada
    image(offscreen, 400, 0)   # mostra a imagem original
```

### Exemplo avançado de máscara

```python
# from https://github.com/py5coding/py5generator/discussions/159#discussioncomment-3567982
import numpy as np

def setup():
    global offscreen, clip_mask, offscreen_alpha_channel
    size(500, 500)
    clip_mask = create_graphics(width, height)
    offscreen = create_graphics(width, height)
    offscreen.begin_draw()
    offscreen.clear()  # fundo transparente
    # offscreen.background(0, 200, 0, 100)  # é possível fundo translúcido
    offscreen.fill(255, 0, 0, 128)  # vermelho translúcido
    for _ in range(100):
        offscreen.rect(random(width), random(height), 50, 50)
    offscreen.end_draw()
    # create a clean copy of the offscreen's alpha channel because the draw() method will ruin it
    offscreen.load_np_pixels()
    offscreen_alpha_channel = offscreen.np_pixels.copy()[:, :, 0]


def draw():
    background(150, 150, 200)
    y = frame_count % height
    line(0, y, width, y)

    clip_mask.begin_draw()
    clip_mask.clear()  # necessary because clip_mask is being recycled
    clip_mask.fill(255)
    clip_mask.circle(mouse_x, mouse_y, 250)
    clip_mask.end_draw()
    clip_mask.load_np_pixels()
    offscreen.load_np_pixels()
    if is_mouse_pressed:
        # calculate the minimum alpha values and set the alpha channel to that
        offscreen.np_pixels[:, :, 0] = np.where(clip_mask.np_pixels[:, :, 0] < offscreen_alpha_channel,
                                                clip_mask.np_pixels[:, :, 0], offscreen_alpha_channel)
    else:
        # copy clip_mask's red channel to offscreen's alpha channel
        offscreen.np_pixels[:, :, 0] = clip_mask.np_pixels[:, :, 1]
    offscreen.update_np_pixels()
    image(offscreen, 0, 0)
```

![offscreen buffer](assets/offscreen_buffer.gif)
