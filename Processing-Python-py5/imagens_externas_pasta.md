
# Lendo todas as imagens de uma pasta

![exemplo de grade de imagens](https: // raw.githubusercontent.com/villares/material-aulas/master/processing-python/assets/muitas_imagens.png)

> exemplo de execução carregando 110 imagens medievais coletadas pelo artista e educador[daniel seda](https: // www.danielseda.com/home).

tendo visto previamente como[ler e usar imagens de arquivos externos](imagens_externas.md) com `load_image()`, e a estrutura de dados lista(`list`) neste exemplo mais avançado vamos permitir que a pessoa escolha uma pasta e o * sketch * vai carregar todas as imagens nela encontradas.

A seleção da pasta começa com uma chamada da função `select_folder()`, quando pressioanada a tecla 'o' (na função de evento `key_pressed()`).

```python


def key_pressed():
    if key == 'o':
        select_folder("Selecione uma pasta", "adicionar_imagens")


```

note que o primeiro argumento de `select_folder()` é `"Selecione uma pasta"` o texto(*string*) que vai como título da janela de seleção. O segundo argumento `"adicionar_imagens"` é mais curioso, trata-se de um * string * com o nome de uma função que será chamada quando a pessoa terminar de interagir com a janela de seleção de pasta(diretório / *folder*). isso é uma estratégia conhecida em programação como designar uma "função de retorno" ou, em inglês, *callback*.

na estratégia com * callback * uma função definida é chamada para nós quando algum evento acontece. neste nosso caso, a função `adicionar_imagens()` é chamada no encerramento da janela de selecionar pastas(esta parte de abrir a janela para selecionar pastas é iniciada com a execução de `select_folder()`, mas o momento do encerramento depende da pessoa usando o programa).

é preciso criar uma variável global para guardar as informações dos arquivos encontrados, fazemos isso com esta linha antes do `setup()` que cria uma lista vazia e aponta o nome `imagens` para ela:

```python
imagens = []
```

A função `adicionar_imagens()` é executada só quando a pessoa terminou de escolher uma pasta ou se tiver cancelado o processo, ela tem um parâmetro `selection` que recebe a pasta selecionada ou o valor especial `None` (se a pessoa fechou a janela sem selecionar uma pasta):

```python


def adicionar_imagens(selection):
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path = selection.get_absolute_path()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in lista_imagens(dir_path):
            img = load_image(file_path)
            img_name = file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))


```

saiba que o código que cuida da janela do sistema operacional para escolhermos a pasta, e também o código da função `adicionar_imagens()`, chamada em seguida, são executados em linhas de execução(*threads*) separadas do * sketch * principal, isto é correm em separado, e por conta disso não interrompem execução do `draw()`, o chamado 'laço principal de repetição' do processing.

O carregamento das imagens é um procedimento razoavelmente lento e por isso é possível vê-las aparecendo aos poucos na tela, conforme são acrescentadas na lista `imagens` pela execução do laço `for` em `adicionar_imagens()`.

uma boa parte da solução da nossa tarefa, na verdade, está encapsulada em `lista_imagens()`, função que usamos em `adicionar_imagens()`. ela recebe o caminho completo da pasta selecionada e devolve uma lista com tuplas dos nomes dos arquivos das imagens e o caminho completo delas para ser usado no `load_image()`:

```python


def lista_imagens(dir=None):
    from os import listdir
    from os.path import isfile, join
    data_path = dir or sketch_path('data')
    try:
        f_list = [(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f)) and imgext(f)]
    except exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list


```
Não vamos entrar em detalhes aqui, mas você pode querer ler mais sobre[compreensão de listas](https: // panda.ime.usp.br/pensepy/static/pensepy/09-listas/listas.html  # list-comprehensions) (a maneira compacta de produzir uma lista usada para criar a `f_list`) e [tratamento de exceções](http://turing.com.br/pydoc/2.7/tutorial/errors.html#excecoes) (o trecho dentro dentro de `try:` e  `except... :`) para entender melhor a função `lista_imagens()`.

repare que usamos a pequena função `has_image_ext()` para responder se  os nomes fornecidos por `os.listdir()` tem a terminação mencionada na tupla `valid_ext`.

```python
def has_image_ext(file_name):
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext=('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    file_ext=file_name.split('.')[-1]
    return file_ext.lower() in valid_ext
```

por fim, aqui vai o código completo do sketch, que desenha uma grade de imagens no `draw()` com os itens da lista `imagens`:

```python
from __future__ import unicode_literals, division

imagens=[]
w, h=80, 55

def setup():
    global colunas, linhas
    size(880, 550)
    colunas, linhas=width // w, height // h
    print('Posições na grade: ' + str(colunas * linhas))

def draw():
    background(0)
    # Desenha grade com `imagens` com colunas fixas de largura `w`, imagens
    # mais largas são sobrepostas
    contador=0
    for c in range(colunas):
        x=c * w
        for l in range(linhas):
            y=l * h
            if contador < len(imagens):
                img=imagens[contador][1]
                fator=h / img.height
                image(img, x, y, img.width * fator, img.height * fator)
                contador += 1

def key_pressed():
    if key == 'o':
        select_folder("Selecione uma pasta", "adicionar_imagens")
    if key == ' ':
        imagens[:]=[]
    if key == 'p':
        save_frame('####.png')

def adicionar_imagens(selection):
    if selection == None:
        print("Seleção cancelada.")
    else:
        dir_path=selection.get_absolute_path()
        print("Pasta selecionada: " + dir_path)
        for file_name, file_path in lista_imagens(dir_path):
            img=load_image(file_path)
            img_name=file_name.split('.')[0]
            print("imagem " + img_name + " carregada.")
            imagens.append((img_name, img))
        print('Número de imagens: ' + str(len(imagens)))

def lista_imagens(dir=None):
    """
    devolve uma a lista de tuplas com os nomes dos arquivos de imagem e os caminhos
    completos para cada uma das images na pasta `dir` ou na pasta /data/ do sketch.
    requer a função has_image_ext() para decidir quais extensões aceitar.
    """
    from os import listdir
    from os.path import isfile, join
    data_path=dir or sketch_path('data')
    try:
        f_list=[(f, join(data_path, f)) for f in listdir(data_path)
                  if isfile(join(data_path, f)) and has_image_ext(f)]
    except exception as e:
        print("Erro ({0}): {1}".format(e.errno, e.strerror))
        return []
    return f_list

def has_image_ext(file_name):
    # extensões dos formatos de imagem que o Processing aceita!
    valid_ext=('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    file_ext=file_name.split('.')[-1]
    return file_ext.lower() in valid_ext
```

uma variante do `draw()` que permite largura variável das imagens, fixando a altura, como no exemplo anterior, mas:

```python
def draw():
    background(0)
    # Desenha `imagens` em filas de altura 'h', deslocando na horizontal com
    # largura de cada imagem.
    x=y=0
    for nome, img in imagens:
        print(img)
        fator=h / img.height
        if x + img.width * fator > width:
            x=0
            y += h
        image(img, x, y, img.width * fator, img.height * fator)
        x += img.width * fator
```

# Assuntos relacionados

- estrutura de pixels das imagens em[pixels e imagens](pixels.md)
- [lendo e escrevendo texto em arquivos(*file IO*)](/processing-python/file_io.md)
