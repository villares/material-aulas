
## Lendo todas as imagens de uma pasta

![exemplo de grade de imagens](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/muitas_imagens.png)

> Exemplo de execução carregando 110 imagens medievais coletadas pelo artista e educador [Daniel Seda](https://www.danielseda.com/home).

Tendo visto previamente como [ler e usar imagens de arquivos externos](imagens_externas.md) com `loadImage()` neste exemplo mais avançado vamos permitir que a pessoa escolha uma pasta e o *sketch* vai carregar todas as imagens nela encontradas.

A seleção da pasta começa com uma chamada da função `selectFolder()`, quando pressioanada a tecla 'o' (na função de evento `keyPressed()`). 

```python
def keyPressed():
    if key == 'o':
        selectFolder("Selecione uma pasta", "adicionar_imagens")
```

Note que o primeiro argumento de `selectFolder()` é `"Selecione uma pasta"` o texto (*string*) que vai como título da janela de seleção. O segundo argumento `"adicionar_imagens"` é mais curioso, trata-se de um *string* com o nome de uma função que será chamada quando a pessoa terminar de interagir com a janela de seleção de pasta (diretório / *folder*). Isso é uma estratégia conhecida em programação como uma *função callback*.

A função `adicionar_imagens()` é executada quando a pessoa terminou de escolher uma pasta ou se tiver cancelado o processo, ela tem um parâmetro `selection` que recebe a pasta selecionada ou o valor especial `None`: 

```python
def adicionar_imagens(selection):
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path = selehrection.getAbsolutePath()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in lista_imagens(dir_path):
            img = loadImage(file_path)
            img_name = file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))
```

Saiba que o código que cuida da janela do sistema operacional para escolhermos a pasta, e também esta função `adicionar_imagens()`, que é chamada em seguida, são executados em linhas de execução (threads) separadas do *sketch* principal, isto é, correm em separado, e por conta disso não interrompem execução do `draw()`, o chamado 'laço principal de repetição' do Processing. 

O carregamento das imagens é um procedimento razoavelmente lento e por isso é possível vê-las aparecendo aos poucos na tela, conforme são acrescentadas na lista global `imagens` pela execução do laço `for` em `adicionar_imagens()`.

Uma boa parte da solução da nossa tarefa, na verdade, está encapsulada em `lista_imagens()`, função que usamos em `adicionar_imagens()`. Ela recebe o caminho completo da pasta selecionada e devolve uma lista com tuplas dos nomes dos arquivos das imagens e o caminho completo delas para ser usado no `loadImage()`: 

```python
def lista_imagens(dir=None):
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketchPath('data')
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f)) and imgext(f)]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list
```
Não vamos entrar em detalhes aqui, mas você pode querer ler mais sobre [compreensão de listas](https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html#list-comprehensions) (a maneira compacta de produzir uma lista usada para criar a `f_list`) e [tratamento de exceções](http://turing.com.br/pydoc/2.7/tutorial/errors.html#excecoes) (o trecho dentro dentro de `try:` e  `except... :`) para entender melhor a função `lista_imagens()`.

Repare que usamos a pequena função `imgext()` para responder se  os nomes fornecidos por `os.listdir()` tem a terminação mencionada na tupla `valid_ext`.

```python
def imgext(file_name):
    ext = file_name.split('.')[-1]
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext = ('jpg',
                 'png',
                 'jpeg',
                 'gif',
                 'tif',
                 'tga',
                 )
    return ext.lower() in valid_ext
```

Por fim, aqui vai o código completo do sketch, que desenha uma grade de imagens no `draw()` com os itens da lista global `imagens`:

```python
from __future__ import unicode_literals , division

imagens = []
w, h = 80, 55

def setup():
    global colunas, linhas
    size(880, 550)
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
        selectFolder("Selecione uma pasta", "adicionar_imagens")
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
        for file_name, file_path in lista_imagens(dir_path):
            img = loadImage(file_path)
            img_name = file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))

def lista_imagens(dir=None):
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
                  if isfile(join(data_path, f)) and imgext(f)]
    except Exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list

def imgext(file_name):
    ext = file_name.split('.')[-1]
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext = ('jpg',
                 'png',
                 'jpeg',
                 'gif',
                 'tif',
                 'tga',
                 )
    return ext.lower() in valid_ext
```

## Assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](/Processing-Python/file_IO.md)
