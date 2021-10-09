## Lendo todas as imagens da pasta `data`

[exemplo de grade de imagens](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/muitas_imagens.png)

> Exemplo de execução usando 110 imagens medievais coletadas pelo artista e educador [Daniel Seda](https://www.danielseda.com/home).

Tendo visto previamente como [ler e usar imagens de arquivos externos](imagens_externas.md) com `loadImage()`, e a estrutura de dados lista (`list`) neste exemplo vamos carregar todas as imagens encontradas na pasta `data` localizada dentro da pasta do seu *sketch*. 

É preciso criar uma variável global para guardar as informações dos arquivos encontrados, fazemos isso com a linha contendo `imagens = []` antes do `setup()` que cria uma lista vazia e aponta o nome `imagens` para ela.

```python
import os  # para usar listdir, path.isfile, path.join

imagens = []  # lista que vai receber objetos PImage (Processing Image data)

def setup():
    size(500, 500)
    # Ponha as imagens na pasta /data/ dentro da pasta do seu sketch
    data_folder = sketchPath('data')  # não funciona fora do setup
    caminhos_arquivos = []
    for nome_arquivo in os.listdir(data_folder):
        caminho_arquivo = os.path.join(data_folder, nome_arquivo)
        if os.path.isfile(caminho_arquivo) and has_image_ext(caminho_arquivo):
            caminhos_arquivos.append(caminho_arquivo)
    for caminho_arquivo in caminhos_arquivos:
        img = loadImage(caminho_arquivo)
        imagens.append(img)
    noLoop()  # clique do mouse para redraw

def draw():
    # from random import choice     # exemplo usando random.choice 
    # random_image = choice(imagens)
    i = int(random(len(imagens)))   # para não usar o random.choice do Python
    random_image = imagens[i]
    image(random_image, 0, 0, width, height)

def mouseClicked():
    redraw()

def has_image_ext(file_name):
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    file_ext = file_name.split('.')[-1]
    return file_ext.lower() in valid_ext
```

## Assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](/Processing-Python/file_IO.md)
