# Exportando animações

Há mais de uma estratégia possível para exportar imagens em movimento, seja em vídeo ou um GIF animado. Um caminho é exportar os diversos frames e usar alguma ferramenta de conversão, o outro é usar uma biblioteca que exporte diretamente um formato desejado.

# Sumário

- A. [Exportando frames](  # a-exportando-frames)
- B. [Biblioteca * GifAnimation*](  # b-biblioteca-gifanimation)
- C. [Biblioteca * Video Export*](  # c-biblioteca-video-export)
- D. [Gravando a tela do computador](  # d-gravando-a-tela-do-computador)

# A. Exportando frames

Podemos usar `save_frame()` dentro do `draw()`, como neste exemplo:

```pyde
diameter=1

def setup():
    size(200, 200)
    smooth()

def draw():
    # o desenho da aminação vai aqui
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter=diameter + 1
    print(frame_count)

    # e no final do draw()
    if frame_count < 250:
        save_frame('imagem####.tga')
    else:
        exit()
```
Para a converter esses 'frames' em um vídeo ou em um GIF animado, podemos usar:
- A ferramenta ** Movie Maker ** do próprio IDE do Processing(Vídeo)
- [**Gimp**](https: // gimp.org) ou [**Glimpse**](http: // https: // glimpse-editor.org /), com o comando 'abrir como camadas' (GIF animado)
- Ferramentas online como ** https: // ezgif.com/** (GIF animado)
- Alguma outra ferramenta da sua escolha, como o[**ffmpeg**](http//www.ffmpeg.org) na linha de comando(ou[via uma GUI](https: // github.com/amiaopensource/ffmpeg-amia-wiki/wiki/3 % 29-Graphical-User-Interface-Applications-using-FFmpeg)).

# B. Biblioteca *GifAnimation*

Infelizmente não está disponível para baixar pelo IDE, é preciso baixar e copiar na pasta de bibliotecas 'manualmente'.

**Passo 1 **
- 1.0 Baixe a biblioteca em: github.com/extrapixel/gif-animation/archive/3.0.zip
- 1.1 Deszipe o aquivo * 3.0.zip *
- 1.2 Copie a pasta * gifAnimation * para dentro da pasta libraries do seu sketchbook(no linux `user/sketchbook/ibraries` no Mac/Win `user/Documents/Processing/libraries`

** Passo 2 **

Copie o código do 'helper', crie no seu sketch no Processing IDE uma aba chamada `gif_export.py` (o IDE adiciona o `.py` pra você) e cole nessa nova aba.

```python
# -*- coding: utf-8 -*-

"""
gif_export.py - a GIF Animation export helper for Processing Python mode - v2020_06_01
Alexandre B A Villares http://abav.lugaralgum.com - Licensed under GPL v3
Inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/

This is for use with the gifAnimation library https://github.com/extrapixel/gif-animation/tree/3.0
Download the library from github.com/extrapixel/gif-animation/archive/3.0.zip
Unzip and copy the gifAnimation folder into your libraries folder, like shown below:
    user/sketchbook/libraries/gifAnimation (Linux) or
    user/Documents/Processing/libraries/gifAnimation (Mac/Windows)

# This file should be saved as a 'tab' named gif_export.py in your Processing Python Mode sketch
# Restart the IDE and add these lines at the start of your sketch:
add_library('gif_animation')
from gif_export import gif_export

# then add this at the end of draw():
gif_export(GifMaker, "filename")

"""

def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=100,
              # quality range 0 - 255 test yourself,my guess is 0 best/high 255
              # worst/low
               delay=170,            # this is quick
               frames=0,             # 0 will stop only if 'e' key pressed
               transparent=None,     # set a transparent color
               finish=False):        # force stop
    global gifExporter
    try:
        gifExporter
    except NameError:
        gifExporter=GifMaker(this, filename + ".gif")
        gifExporter.setRepeat(repeat)
        gifExporter.setQuality(quality)
        gifExporter.setDelay(delay)
        if transparent is not None:
            gifExporter.setTransparent(transparent)
        print("gif recording started")

    gifExporter.addFrame()

    if frames == 0:
       if keyPressed and key == 'e':
           finish=True
    elif frameCount >= frames:
        finish=True

    if finish:
        gifExporter.finish()
        print("gif saved, exit")
        exit()

```

** Passo 3 **

Exemplo de uso, este é o código que vai na primeira aba, a principal, do IDE.

![exemplo de exportação de gif](assets/exported.gif)

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
add_library('gif_animation')
from gif_export import gif_export

diameter=1

def setup():
    size(200, 200)
    smooth()

def draw():
    # your animation drawing goes here
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter=diameter + 1
    print(frameCount)
    # then add this line at the end of draw()
    gif_export(GifMaker, frames=250)
```


# C. Biblioteca *Video Export*

A biblioteca * Video Export * criada por Abe Pazos[@hamoid](https: // github.com/hamoid) pode ser baixada diretamente pelo IDE, e vem com vários exemplos. Será necessário instalar a ferramenta `ffmpeg` disponível em[www.ffmpeg.org](https: // www.ffmpeg.org /)

**[Falta alertar sobre a installação do ffmpeg] **

```python
"""
Exemplo de uso da biblioteca Video Export de Abe Pazos
Baixe no pelo menu do IDE: Sketch > Importar Biblioteca... > Adicionar Biblioteca...
É preciso instalar ffmpeg: https://www.ffmpeg.org/
"""

add_library('VideoExport')
gravando=False

def setup():
    global video_export
    size(600, 600)
    noStroke()
    frameRate(30)

    println(u"Aperte 'r' para iniciar e parar a gravação")
    println(u"Aperte 'q' para encerrar o programa e fechar o arquivo")

    video_export=VideoExport(this, "animacao.mp4")
    video_export.setFrameRate(30)  # reduz a taxa de quadros (opcional)
    frameRate(30)
    # Qualidade máxima de vídeo: 100. Audio ótimo: 256 / muito bom: 192
    video_export.setQuality(70, 128)  # qualidade default de vídeo e audio
    video_export.startMovie()


def draw():
    background(0)
    t=frameCount * 0.03
    sz=100 + 50 * cos(t * 1.33) * cos(t * 1.84)
    ellipse(300 + 200 * cos(t * 1.13) * cos(t * 0.21),
            300 + 200 * cos(t * 1.71) * cos(t * 0.47),
            sz, sz)
    if gravando:
        video_export.saveFrame()

def keyPressed():
    global gravando
    if key == 'r' or key == 'R':
        gravando=not gravando
        println(u"A gravação está {}".format(
            "LIGADA" if video_export else "DESLIGADA"))

    if key == 'q' or key == 'Q':
        video_export.endMovie()
        exit()

```
# D. Gravando a tela do computador

Uma última estratégia que pode ser útil para documentar e compartilhar o resultado de * sketches * é gravar a tela do computador, ou parte dela.

- [Peek](https: // github.com/phw/peek) - Linux - exporta diretamente GIF, APNG ou MP4
- [LICEcap](https: // www.cockos.com/licecap /) - Windows e MacOS - exporta diretamenteGIF
- [OBS Studio](https: // obsproject.com /) - Windows, MacOS e Linux - exporta vídeo
- [GifCam](https: // gifcam.br.uptodown.com/windows) - Windows - exporta e edita diretamenteGIF
