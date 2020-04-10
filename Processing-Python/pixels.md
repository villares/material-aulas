# Pixels e imagens
> Baseado em **arteprog** Programação Criativa / [Pixel e imagens](https://github.com/arteprog/programacao-criativa/blob/master/conteudo/pixels-e-imagens.md)

Uma imagem digital, por vezes chamada de uma imagem bitmap, nada mais é do que uma sequência de números indicando variações de vermelho, verde e azul numa localização particular de uma grade de ***pixels***, um neologismo cunhado na década de 60 juntado *pix*, abreviação de *picture*, e *el* de *element*, é o menor elemento de uma imagem.

A maior parte do tempo nós visualizamos esses pixels como retângulos miniatura justapostos na tela do computador. No entanto, com um pouco de pensamento criativo e com a manipulação dos pixels com código, podemos mostrar esta informação de inúmeras maneiras. Apesar disso, de tempos em tempos, podemos querer quebrar nossa rotina de desenho corriqueira e manipular os pixels da tela diretamente. O Processing proporciona isso através de um **array** de pixels.

Estamos acostumados com a ideia de cada pixel na tela ter uma posição X e Y numa janela. No entanto, um array de pixels tem apenas uma dimensão, armazenado os valores de cor numa sequência linear.
        
Como os pixels aparecem:

| 0 | 1 | 2 | 3 | 4 |
| -= 1 | -= 1- | -= 1- | -= 1- | -= 1- |
| **5** | **6** | **7** | **8** | **9** |
| **10** | **11** | **12** | **13** | **14** |
| **15** | **16** | **17** | **18** | **19** |
| **20** | **21** | **22** | **23** | **24** |


Como os pixels são armazenados:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | ... | 24 |
| -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- | -= 1- |
| |

### Acessando os pixels numa posição X e Y

Use `get()` para os pixels visveis na tela ou o método `.get()` para os pixels em uma imagem `PImage`.

```pyde

def setup():
    global img
    size(400, 400)
    noStroke()
    rectMode(CENTER)
    img = loadImage("ale.jpg")     # carregando uma imagem da pasta /data/


def draw():
    image(img, 0, 0)    # desenha a imagem (PImage, x, y, [largura, altura]*) *opcionais 
    cor = img.get(mouseX, mouseY) # pega a cor do pixel na posição x, y
    R = red(img.get(mouseX, mouseY)) # pega a quantidade de vermelho do pixel na posição x, y
    G = green(img.get(mouseX, mouseY)) # pega a quantidade de verde do pixel na posição x, y
    B = blue(img.get(mouseX, mouseY)) # pega a quantidade de azul do pixel na posição x, y
    fill(cor)    # pede o preenchimento!
    ellipse(mouseX, mouseY, 60, 60) # desenha um círculo
    fill(255, 0, 0) # vermelho
    rect(mouseX, mouseY + 60, R, 20) 
    fill(0, 255, 0) # verde
    rect(mouseX, mouseY + 80, G, 20)
    fill(0, 0, 255) # azul
    rect(mouseX, mouseY + 100, B, 20)


```

![](https://github.com/arteprog/programacao-criativa/blob/master/assets/imagens/get008.jpg?raw=True) ![](https://github.com/arteprog/programacao-criativa/blob/master/assets/imagens/get017.jpg?raw=True)

### Manipulando individualmente os pixels de uma imagem 

O método `loadPixels()` dá acesso a um array contendo os pixels da imagem e `updatePixels()` atualiza na imagem modificações que tenham sido feitas no array.

Use `createImage()` para criar um novo objeto `PImage` (tipo de dados para armazenar imagens) vazio, fornecendo assim um buffer de pixels que pode ser manipulado.

```
createImage(w, h, formato) # w (largura em pixels), h (altura em pixels),
             # formato (RGB, ARGB ou ALPHA: canal alpha em escala de cinzas)        
```

```pyde

def setup():
    global img # define um objeto PImage chamado imagem 
    global imgAux # define um objeto PImage chamado imagem auxiliar
    img = loadImage("flor.jpg") # carrega uma imagem
    imgAux = img # carrega a imagem auxiliar
    surface.setSize(img.width * 2, img.height) # defini o tamanho da tela

def draw():
    background(255)
    image(img, 0, 0)
    image(imgAux, img.width, 0)


def keyPressed():
    img.loadPixels()
    imgAux.loadPixels()
    PImage foto = createImage(img.width, img.height, RGB)
    foto.loadPixels()

    if key == '1':
        origem = img.width * img.height
        # multiplicar a largura pela altura para encontrar o último pixel
        destino = 0     
        for (temp = origem-1 temp>=0 temp-= 1) :
        # origem -1 pq começamos contar do 0
            foto.pixels[destino] = img.pixels[temp]
            destino += 1
    
    imgAux = foto
    imgAux.updatePixels()
```

![](https://github.com/arteprog/programacao-criativa/blob/master/assets/imagens/pixel01.png?raw=True)

```pyde
def setup() :
    global img, imgTemp
    size(800, 400)
    img = loadImage("monica.jpg")
    imgTemp = img.get()

def draw() :
    scale(2)
    image(img,0,0)
    image(imgTemp, img.width, 0)
    for i in range(len(imgTemp.pixels)):
        record = -1 
        selectedPixel = i 
        for j in range i j < imgTemp.pixels.length j+= 1) :
            color pix     = imgTemp.pixels[j] 
            b = hue(pix) 
            if (b > record) :
                selectedPixel = j 
                record = b    
        
        cor = imgTemp.pixels[i]
        imgTemp.pixels[i] = imgTemp.pixels[selectedPixel]
        imgTemp.pixels[selectedPixel] = cor
    
    imgTemp.updatePixels()
```

![](https://github.com/arteprog/programacao-criativa/blob/master/assets/imagens/pixe02.png?raw=True)

## Filtros de imagem

Processing oferece uma série de filtros prontos que podem ser aplicados em qualquer imagem. O comando filtro() aplica um filtro em uma imagem usando a sintaxe `filter(MODE)` ou `filter(MODE, level)`

### Modos disponíveis como parâmetros de filter()

THRESHOLD: Converte a imagem em pixels pretos ou brancos, dependendo se eles estão acima ou abaixo do limite definido pelo parâmetro de nível. O nível deve estar entre 0,0 (preto) e 1,0 (branco). Se nenhum nível for especificado, 0,5 será usado.
```pyde
img = loadImage("exemplo.jpg")
image(img, 0, 0)
filter(THRESHOLD)
```
        
`GRAY`: Converte as cores na imagem em equivalentes de escala de cinza. Nenhum parâmetro é usado.

`INVERT`: Define cada pixel para o seu valor inverso. Nenhum parâmetro é usado.

`POSTERIZE`: Limita cada canal da imagem ao número de cores especificado como parâmetro. O parâmetro pode ser configurado para valores entre 2 e 255, mas os resultados são mais visíveis nos intervalos inferiores.

`BLUR`: executa um borramento Gaussiano (n.t. Guassian blur), sendo que o parâmetro level especifica a extensão do borramento. Nos casos em que o parâmetro level não é utilizado, o borramento equivalente a um borramento gaussiano de raio 1.

`OPAQUE`: Define o canal alfa de forma totalmente opaca. Nenhum parâmetro é usado.

`ERODE`: Reduz as áreas de luz. Nenhum parâmetro é usado.

`DILATE`: Aumenta as áreas de luz. Nenhum parâmetro é usado.

# Manipulação de bits em Pixels

O valor de um pixel é representado no Processing (e no Java) como um número inteiro. Nesse sentido, uma imagem digital é um array de números inteiros, como vimos acima. Um inteiro é composto de 32 bits ou 4 bytes para armazenar a informação sobre a cor dos pixels. Especificamente, o primeiro byte (ou seja, 8 bits - um número entre 0 and 255) armazena o grau de transparência (canal alpha), o segundo byte para vermelho, terceiro byte para verde e o quarto byte para azul. Esquematicamente, os bits de inteiros, representando um pixel, aparecem assim:


| Alpha | Vermelho | Verde | Azul |
| -= 1-    | -= 1-    | -= 1- | -= 1- |
| 00000000 | 00000000 |    00000000 | 00000000 |

Esses valores podem ser manipulados com "bit shifting". Isso significa que para acessar uma cor, nós precisamos mexer no nível dos bits para extrair os 8 bits específicos que desejamos.    
