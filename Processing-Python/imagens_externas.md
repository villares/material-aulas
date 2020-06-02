# Como usar imagens externas

## Acessando um arquivo com `loadImage()`

Podemos carregar (*load*) na memória imagens digitais a partir de arquivos externos nos formatos PNG, JPG, GIF, TIF entre outros. Para isso usamos a função `loadImage()`, mas é preciso indicar onde está o arquivo (o chamado 'caminho completo' do arquivo), ou que ele esteja na pasta `/data/` dentro da pasta do seu *sketch* (programa).

```
sketch_2020_04a                (pasta/folder do sketch)
  L  sketch_2020_04a.pyde      (arquivo com o código)
  L  data                      (pasta/folder)
       L  imagem.jpg           (imagem)
```

Note que a operação de carregar o arquivo de imagem é relativamente demorada e nunca deve ser executada dentro do laço `draw()`. Em geral só precisamos carregar uma vez a imagem e fazemos isso no `setup()`. Também é comum criarmos uma variável global que faz referência à imagem, neste exemplo a variável `img`:

```pyde
def setup():
    size(400, 400)
    global img
    img = loadImage("image.jpg")  # arquivo JPG na pasta /data/


def draw():
    image(img, 0, 0)  # é possível forçar um tamanho com image(imagem, 0, 0, 100, 100)
    # img.width e img.height são as dimensões da imagem original
    # podemos mostrar uma imagem com metade da sua largura e altura originais assim:
    # image(img, 0, 0, img.width / 2, img.height / 2)
    
```

Se a imagem tiver **exatamente** a mesma dimensão da área de desenho ela pode ser usada em `background()`.

```pyde
def setup():
    size(600, 400)
    global imagem_fundo
    imagem_fundo = loadImage("fundo.png")  #  fundo tem que ter exatamente 600x400 pixels

def draw():
    background(imagem_fundo)
    # outros desenhos sobre o fundo aqui
```

Pode ser conveniente simplesmente usar a função `image()` como visto anteriormente, para desenhar a imagem na área de desenho logo no começo do `draw()`, caso suas dimensões não sejam iguais a área de desenho.

```pyde
def setup():
    size(600, 400)
    global imagem_fundo
    imagem_fundo = loadImage("fundo.png")

def draw():
    image(imagem_fundo, 0, 0, width, height)  # vai forçar/distorcer o tamanho na imagem
    # ou usamos image(imagem_fundo, 0, 0) mas pode faltar ou sobrar imagem em relação à área.
    # outros desenhos sobre o fundo aqui
```

### Acessando a cor de um pixel da tela ou de uma imagem

Use `get()` para os pixels visíveis na tela ou o método `.get()` para os pixels em uma imagem `PImage`. Como no exemplo abaixo:

```pyde
 def setup():
    size(500,500)
    global imagem
    imagem = loadImage('arquivo.png')  # carregando uma imagem da pasta /data/
    
 def draw():
    iw, ih = imagem.width, imagem.height
    print(iw, ih)
    cor = imagem.get(mouseX, mouseY)  # cor do pixel sob o mouse
    fill(cor)
    noStroke()
    image(imagem, 0, 0)
    circle(mouseX, mouseY, 30)
```

## Assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Exportando imagens](exportando_imagem.md)
