# Exportando animações

Há mais de uma estratégia possível para exportar imagens em movimento, seja em vídeo ou um GIF animado. Um caminho é exportar os diversos frames e usar alguma ferramenta de conversão, o outro é usar uma ferramenta que exporte diretamente um formato desejado.


# A. Exportando frames

Podemos usar `save_frame()` dentro do `draw()`, como neste exemplo:

```python
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
- A ferramenta ** Movie Maker ** do IDE do Processing(Vídeo)
- [**Gimp**](https://gimp.org) ou [**Glimpse**](http://https://glimpse-editor.org /), com o comando 'abrir como camadas' (GIF animado)
- Ferramentas online como ** https://ezgif.com/** (GIF animado)
- Alguma outra ferramenta da sua escolha, como o[**ffmpeg**](http//www.ffmpeg.org) na linha de comando(ou[via uma GUI](https://github.com/amiaopensource/ffmpeg-amia-wiki/wiki/3 % 29-Graphical-User-Interface-Applications-using-FFmpeg)).
- Um script Python que combina PNGs usando Pillow.


```
#! /usr/bin/python3
"""
Cria GIF a partir de todos os arquivos PNG no mesmo diretório (ou chame com -h na linha de comando para configurar).  
"""
from pathlib import Path
from PIL import Image, GifImagePlugin
import argparse

parser = argparse.ArgumentParser(prog='PNG frames to GIF animation')
parser.add_argument('-i', '--input', help='Input folder containing the PNG images')
parser.add_argument('-o', '--output', default='output.gif', help='Output GIF file name')
parser.add_argument('-d', '--duration', default=200, type=int, help='Frame duration in milliseconds')
parser.add_argument('-NO', '--no-optimization', action='store_true', help='Turn off optimization')
parser.add_argument('-l', '--loop', default=0, type=int, help='Number of loops (default=0, keep looping)')

args = parser.parse_args()

input_dir = Path(args.input or Path.cwd())
if input_dir.is_dir():
    images = [Image.open(file_path) for file_path
              in sorted(input_dir.iterdir())
              if file_path.suffix.lower() == '.png']
    if images:
        output_path = input_dir / args.output
        images[0].save(
            output_path,
            save_all=True, append_images=images[1:],
            optimize=not args.no_optimization,
            duration=args.duration,
            loop=args.loop
            )
        print(f'Animation saved at:\n'
              f'{output_path}\n'
              #f'Optimization: {not args.no_optimization}'
              )
    else:
        print(f'No PNG images found at:\n{input_dir}')
else:
    print(f'{input_dir}\nis not a valid input dir.')
`
```

# B. Exportação de GIF pelo py5

- https://py5coding.org/reference/py5tools_animated_gif.html

# C. Gravando a tela do computador

Uma última estratégia que pode ser útil para documentar e compartilhar o resultado de *sketches* é gravar a tela do computador, ou parte dela.

- ~~[Peek](https://github.com/phw/peek) - Linux - exporta diretamente GIF, APNG ou MP4~~ parou de funcionar
- [Blue Recorder](https://github.com/xlmnxp/blue-recorder/) - Linux - exporta vídeos e GIF
- [LICEcap](https://www.cockos.com/licecap /) - Windows e MacOS - exporta GIF
- [OBS Studio](https://obsproject.com /) - Windows, MacOS e Linux - exporta vídeos
- [GifCam](https://gifcam.br.uptodown.com/windows) - Windows - exporta e edita GIF
