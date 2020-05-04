## Lendo todas as imagens de uma pasta

![exemplo de grade de imagens](assets/muitas_imagens.png)

> Exemplo de execução carregando 110 imagens medievais coletadas pelo artista e educador [Daniel Seda](https://www.danielseda.com/home).

Tendo visto previamente como [ler e usar imagens de arquivos externos](imagens_externas.md) com `loadImage()` neste exemplo mais avançado vamos permitir que a pessoa escolha uma pasta e o *sketch* vai carregar todas as imagens nela encontradas.

A seleção da pasta começa quando a tecla 'o' é apertada e a função `selectFolder()` é chamada. 

```python
def keyPressed():
    if key == 'o':
        selectFolder("Selecine uma pasta", "adicionar_imagens")
```

Note que o primeiro argumento de `selectFolder()` é `"Selecine uma pasta"` o texto (*string*) que vai como título da janela de seleção. O segundo argumento `"adicionar_imagens"` é mais curioso, trata-se de um *string* com o nome de uma função que será chamada quando a pessoa terminar de interagir com a janela de seleção de pasta (diretório / *folder*). Essa função `adicionar_imagens()` vai ser executada seja quando a pessoa terminou de escolher a pasta ou se tiver cancelado o processo. Veja a seguir a definição da função:

```python
def adicionar_imagens(selection):
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path = selection.getAbsolutePath()
        print("Pasta selecionada: " + dir_path)
        for img_name, img_file in list_images(dir_path):
            img = loadImage(img_file)
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))
```

Saiba que o código que cuida da janela do sistema operacional para escolhermos a pasta e também esta função, chamada em seguida, são executados em *threads* separadas do *sketch* principal, e por conta disso não interrompem a repetida execução de `draw()`. Note como o carregamento das imagens é um procedimento razoavelmente lento e é possível vê-las aparecendo aos poucos na tela, conforme são acrescentadas na lista global `imagens` pela execução do laço `for` em `adicionar_imagens()`.

Uma boa parte da solução está encapsulada em `list_images()`, usada em `adicionar_imagens()`, uma função que recebe o caminho completo da pasta selecionada e devolve uma lista com tuplas dos nomes dos arquivos das imagens e o caminho completo delas para ser usado no `loadImage()`. 

```python
def list_images(dir=None):
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketchPath('data')
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f))
                  and imgext(f)]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list
```

Repare que `list_images()` depende da pequena função `imgext()` que responde se o nome da lista produzida por `os.listdir()` tem uma terminação mencionada na tupla `extensions`.

```python
def imgext(file_name):
    extensions = ('.jpg',
                  '.png',
                  '.jpeg',
                  '.gif',
                  '.tif',
                  '.tga',
                  )
    for ext in extensions:
        if file_name.endswith(ext):
            return True
    return False
```

Aqui o código completo do sketch:

```python
from __future__ import unicode_literals , division

imagens = []
w, h = 77, 55

def setup():
    global colunas, linhas
    size(770, 550)
    colunas, linhas = width // w, height // h
    print('Posições na grade: ' + str(colunas * linhas))
    
def draw():
    background(0)
    contador = 0
    # Desenha uma grade com as imagens na lista `imagens`
    for c in range(colunas):
        x = c * w
        for l in range(linhas):
            y = l * h
            if contador < len(imagens):
                img = imagens[contador][1]
                fator = h / img.height
                image(img, x, y, img.width * fator, img.height * fator)
                contador += 1
    
def keyPressed():
    if key == 'o':
        selectFolder("Selecine uma pasta:", "adicionar_imagens")
    if key == ' ':
        imagens[:] = []
    if key == 'p':
        saveFrame('####.png')

def adicionar_imagens(selection):
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path = selection.getAbsolutePath()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in list_images(dir_path):
            img = loadImage(file_path)
            img_name = file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))


def list_images(dir=None):
    """
    Devolve uma a lista de tuplas com os nomes dos arquivos de imagem e os caminhos
    completos para cada uma das images na pasta `dir` ou na pasta /data/ do sketch.
    Requer a função imgext() para decidir quais extensões aceitar.
    """
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketchPath('data')
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f))
                  and imgext(f)]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list

def imgext(file_name):
    extensions = ('.jpg',
                  '.png',
                  '.jpeg',
                  '.gif',
                  '.tif',
                  '.tga',
                  )
    for ext in extensions:
        if file_name.endswith(ext):
            return True
    return False
```

## Assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](/Processing-Python/file_IO.md)
