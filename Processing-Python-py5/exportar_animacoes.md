# Exportando animações

Há mais de uma estratégia possível para exportar imagens em movimento, seja em vídeo ou um GIF animado. Um caminho é exportar os diversos frames e usar alguma ferramenta de conversão, o outro é usar uma ferramenta que exporte diretamente um formato desejado.


# A. Exportando frames

Podemos usar `save_frame()` dentro do `draw()`, como neste exemplo:

```python
diameter = 1

def setup():
    size(200, 200)
    smooth()

def draw():
    # o desenho da aminação vai aqui
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter = diameter + 1
    # e no final do draw()
    if frame_count < 250 and frame_count % 2 == 1:
        print(frame_count)
        save_frame('imagem####.tga')
    else:
        exit_sektch()
```
Para a converter esses 'frames' em um vídeo ou em um GIF animado, podemos usar:
- A ferramenta **Movie Maker** do IDE do Processing (Vídeo)
- [**Gimp**](https://gimp.org) com o comando 'abrir como camadas' (GIF animado)
- Ferramentas online como **https://ezgif.com/** (GIF animado)
- Alguma outra ferramenta da sua escolha, como o [**ffmpeg**](http//www.ffmpeg.org) na linha de comando (ou[via uma GUI](https://github.com/amiaopensource/ffmpeg-amia-wiki/wiki/3 % 29-Graphical-User-Interface-Applications-using-FFmpeg)).
- Um script Python que combina PNGs usando `imageio`, [na linha de comando](https://github.com/villares/sketch-a-day/blob/main/admin_scripts/pngs_to_gif.py) ou [com GUI](https://github.com/villares/sketch-a-day/blob/main/admin_scripts/pngs_to_gif_gui.py).

# B. Exportação de GIF pelo py5

- https://py5coding.org/reference/py5tools_animated_gif.html

# C. Gravando a tela do computador

Uma última estratégia que pode ser útil para documentar e compartilhar o resultado de *sketches* é gravar a tela do computador, ou parte dela.

- [pypeek](https://github.com/firatkiral/pypeek) - Linux, Windows e Mac, exporta GIF e mp4.
- [Blue Recorder](https://github.com/xlmnxp/blue-recorder) - Linux - exporta GIF e vídeos.
- [LICEcap](https://www.cockos.com/licecap) - Windows e MacOS - exporta GIF
- [OBS Studio](https://obsproject.com) - Windows, MacOS e Linux - exporta vídeos
- [GifCam](https://gifcam.br.uptodown.com/windows) - Windows - exporta e edita GIF
