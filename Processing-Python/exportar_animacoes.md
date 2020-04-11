# Exortando animações

Há mais de uma estratégia possível para exportar imgagens em movimentoe, seja em vídeo ou um GIFs animado. Um caminho é exportar os diversos frames e usar alguma ferramenta de conversão, o outro é usar uma biblioteca que exporte diretamente um formato desejado.

### A. Exportando frames estáticos

Podemos usar `saveFrame()` dentro do `draw()`, como neste exemplo:

```pyde
diameter = 1

def setup():
    size(200, 200)
    smooth()

def draw():
    # o desenho da aminação vai aqui
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter = diameter + 1
    print(frameCount)
    
    # e no final do draw()
    if frameCount < 250:
        saveFrame('imagem####.tga')
    else:
        exit()
```
Para a conversão, a própria ferramenta `Movie Maker` do IDE do Processing, Gimp a partir de 'abrir como camadas' ou outra ferramenta da sua escolha (ffmpeg na linha de comando?).

### B. Biblioteca *GifAnimation*
    
Infelizmente não está disponível para baixar pelo IDE, é preciso baixar e copiar na pasta de bibliotecas 'manualmente'.

**Passo 1**
1.0 Baixar aqui a lib: github.com/extrapixel/gif-animation/archive/3.0.zip
1.1 deszipar
1.2 copiar a pasta gifAnimation para dentro da pasta libraries do seu sketchbook (no linux `user/sketchbook/ibraries` no Mac/Win `user/Documents/Processing/libraries`

**Passo 2** 

Copie o código do 'helper', crie no seu sketch no Processing IDE uma aba chamada `gif_export.py` (o IDE adiciona o `.py` pra você) e cole nessa nova aba.

```python
"""
This is a helper for the Processing gifAnimation library
https://github.com/extrapixel/gif-animation/tree/3.0

Download the library from github.com/extrapixel/gif-animation/archive/3.0.zip 
Unzip and copy the gifAnimation folder into your libraries folder, like shown below:
user/sketchbook/libraries/gifAnimation (Linux) 
user/Documents/Processing/libraries/gifAnimation (Mac/Windows) 

# Restart the IDE and add these lines at the start of your sketch:
add_library('gifAnimation')
from gif_export import gif_export
# then add this at the end of draw():
gif_export(GifMaker, "filename")
"""

def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=255,          # quality range 0 - 255
               delay=170,            # this is quick
               frames=0,             # 0 will stop only if 'e' key pressed
               finish=False):        # force stop
    global gifExporter
    try:
        gifExporter
    except NameError:
        gifExporter = GifMaker(this, filename + ".gif")
        gifExporter.setRepeat(repeat)
        gifExporter.setQuality(quality)
        gifExporter.setDelay(delay)
        print("gif recording started")

    gifExporter.addFrame()

    if frames == 0:
       if keyPressed and key=='e':
           finish = True
    elif frameCount >= frames:
        finish = True
                
    if finish:
        gifExporter.finish()
        print("gif saved, exit")
        exit()
```

**Passo 3**

Exemplo de uso, este é o código que vai na primeira aba, a principal, do IDE.

```python
"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

Testing the Processing GifMaker Gif Animation library
github.com/extrapixel/gif-animation/tree/3.0
Download the library from:
https://github.com/extrapixel/gif-animation/archive/3.0.zip
Download the gif_export.py helper from:
https://github.com/villares/py.processing-play/blob/master/py_gif_animation_test/gif_export.py
Read the comments inside gif_export.py!
"""

# add the following 2 lines
add_library('gifAnimation')
from gif_export import gif_export

diameter = 1

def setup():
    size(200, 200)
    smooth()

def draw():
    # your animation drawing goes here
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter = diameter + 1
    print(frameCount)
    # then add this line at the end of draw()
    gif_export(GifMaker, frames=250)
```
    
### C. Biblioteca *Video Export*
    
Pode ser baixada diretamente pelo IDE, e vem com exemplos.
    


