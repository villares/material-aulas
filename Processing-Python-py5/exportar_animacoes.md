# Exportando animações

Há mais de uma estratégia possível para exportar imagens em movimento, seja em vídeo ou um GIF animado. um caminho é exportar os diversos frames e usar alguma ferramenta de conversão, o outro é usar uma biblioteca que exporte diretamente um formato desejado.

# Sumário

- a. [exportando frames](  # a-exportando-frames)
- b. [biblioteca * gif_animation*](  # b-biblioteca-gifanimation)
- c. [biblioteca * video export*](  # c-biblioteca-video-export)
- d. [gravando a tela do computador](  # d-gravando-a-tela-do-computador)

# A. Exportando frames

podemos usar `save_frame()` dentro do `draw()`, como neste exemplo:

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
para a converter esses 'frames' em um vídeo ou em um GIF animado, podemos usar:
- A ferramenta ** movie maker ** do próprio IDE do processing(Vídeo)
- [**gimp**](https: // gimp.org) ou [**glimpse**](http: // https: // glimpse-editor.org /), com o comando 'abrir como camadas' (GIF animado)
- ferramentas online como ** https: // ezgif.com/** (GIF animado)
- alguma outra ferramenta da sua escolha, como o[**ffmpeg**](http//www.ffmpeg.org) na linha de comando(ou[via uma GUI](https: // github.com/amiaopensource/ffmpeg-amia-wiki/wiki/3 % 29-graphical-user-interface-applications-using-f_fmpeg)).

# B. Biblioteca *GifAnimation*

infelizmente não está disponível para baixar pelo IDE, é preciso baixar e copiar na pasta de bibliotecas 'manualmente'.

**passo 1 **
- 1.0 baixe a biblioteca em: github.com/extrapixel/gif-animation/archive/3.0.zip
- 1.1 deszipe o aquivo * 3.0.zip *
- 1.2 copie a pasta * gif_animation * para dentro da pasta libraries do seu sketchbook(no linux `user/sketchbook/ibraries` no mac/win `user/documents/processing/libraries`

** passo 2 **

copie o código do 'helper', crie no seu sketch no processing IDE uma aba chamada `gif_export.py` (o IDE adiciona o `.py` pra você) e cole nessa nova aba.

```python
# -*- coding: utf-8 -*-

"""
gif_export.py - a GIF animation export helper for processing python mode - v2020_06_01
alexandre B A villares http://abav.lugaralgum.com - licensed under GPL v3
inspired by an example by art simon https://github.com/apcs_principles/animated_gif/

this is for use with the gif_animation library https://github.com/extrapixel/gif-animation/tree/3.0
download the library from github.com/extrapixel/gif-animation/archive/3.0.zip
unzip and copy the gif_animation folder into your libraries folder, like shown below:
    user/sketchbook/libraries/gif_animation (linux) or
    user/documents/processing/libraries/gif_animation (mac/windows)

# This file should be saved as a 'tab' named gif_export.py in your Processing Python Mode sketch
# Restart the IDE and add these lines at the start of your sketch:
add_library('gifAnimation')
from gif_export import gif_export

# then add this at the end of draw():
gif_export(gif_maker, "filename")

"""

def gif_export(gif_maker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=100,
              # quality range 0 - 255 test yourself,my guess is 0 best/high 255
              # worst/low
               delay=170,            # this is quick
               frames=0,             # 0 will stop only if 'e' key pressed
               transparent=None,     # set a transparent color
               finish=False):        # force stop
    global gif_exporter
    try:
        gif_exporter
    except name_error:
        gif_exporter=gif_maker(this, filename + ".gif")
        gif_exporter.set_repeat(repeat)
        gif_exporter.set_quality(quality)
        gif_exporter.set_delay(delay)
        if transparent is not None:
            gif_exporter.set_transparent(transparent)
        print("gif recording started")

    gif_exporter.add_frame()

    if frames == 0:
       if key_pressed and key == 'e':
           finish=True
    elif frame_count >= frames:
        finish=True

    if finish:
        gif_exporter.finish()
        print("gif saved, exit")
        exit()

```

** passo 3 **

exemplo de uso, este é o código que vai na primeira aba, a principal, do ide.

![exemplo de exportação de gif](assets/exported.gif)

```python
"""
alexandre B A villares http://abav.lugaralgum.com - GPL v3

testing the processing gif_maker gif animation library
github.com/extrapixel/gif-animation/tree/3.0
download the library from:
https://github.com/extrapixel/gif-animation/archive/3.0.zip
download the gif_export.py helper from:
https://github.com/villares/py.processing-play/blob/master/py_gif_animation_test/gif_export.py
read the comments inside gif_export.py!
"""

# add the following 2 lines
add_library('gifAnimation')
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
    print(frame_count)
    # then add this line at the end of draw()
    gif_export(gif_maker, frames=250)
```


# C. Biblioteca *Video Export*

A biblioteca * video export * criada por abe pazos[@hamoid](https: // github.com/hamoid) pode ser baixada diretamente pelo IDE, e vem com vários exemplos. será necessário instalar a ferramenta `ffmpeg` disponível em[www.ffmpeg.org](https: // www.ffmpeg.org /)

**[falta alertar sobre a installação do ffmpeg] **

```python
"""
exemplo de uso da biblioteca video export de abe pazos
baixe no pelo menu do IDE: sketch > importar biblioteca... > adicionar biblioteca...
é preciso instalar ffmpeg: https://www.ffmpeg.org/
"""

add_library('VideoExport')
gravando=False

def setup():
    global video_export
    size(600, 600)
    no_stroke()
    frame_rate(30)

    print(u"Aperte 'r' para iniciar e parar a gravação")
    print(u"Aperte 'q' para encerrar o programa e fechar o arquivo")

    video_export=video_export(this, "animacao.mp4")
    video_export.set_frame_rate(30)  # reduz a taxa de quadros (opcional)
    frame_rate(30)
    # Qualidade máxima de vídeo: 100. Audio ótimo: 256 / muito bom: 192
    video_export.set_quality(70, 128)  # qualidade default de vídeo e audio
    video_export.start_movie()


def draw():
    background(0)
    t=frame_count * 0.03
    sz=100 + 50 * cos(t * 1.33) * cos(t * 1.84)
    ellipse(300 + 200 * cos(t * 1.13) * cos(t * 0.21),
            300 + 200 * cos(t * 1.71) * cos(t * 0.47),
            sz, sz)
    if gravando:
        video_export.save_frame()

def key_pressed():
    global gravando
    if key == 'r' or key == 'R':
        gravando=not gravando
        print(u"A gravação está {}".format(
            "LIGADA" if video_export else "DESLIGADA"))

    if key == 'q' or key == 'Q':
        video_export.end_movie()
        exit()

```
# D. Gravando a tela do computador

uma última estratégia que pode ser útil para documentar e compartilhar o resultado de * sketches * é gravar a tela do computador, ou parte dela.

- [peek](https: // github.com/phw/peek) - linux - exporta diretamente GIF, APNG ou MP4
- [lic_ecap](https: // www.cockos.com/licecap /) - windows e mac_os - exporta diretamente_gif
- [OBS studio](https: // obsproject.com /) - windows, mac_os e linux - exporta vídeo
- [gif_cam](https: // gifcam.br.uptodown.com/windows) - windows - exporta e edita diretamente_gif
