## Lendo todas as imagens da pasta `data`

![imagens sorteadas da pasta](assets/random_images.gif)

> Exemplo de execução usando imagens medievais coletadas pelo artista e educador [Daniel Seda](https://www.danielseda.com/).

Tendo visto previamente como [ler e usar imagens de arquivos externos](imagens_externas.md) com `load_image()`, e a estrutura de dados lista (`list`) neste exemplo vamos carregar todas as imagens encontradas na pasta `data` localizada dentro da pasta do seu *sketch*. Depois vamos "sortear", uma imagem para mostrar usando a função `random.choice`. A cada clique do mouse uma nova imagem será mostrada.

Para começar, é preciso criar uma variável global para guardar os dados das imagens carregados dos arquivos encontrados, fazemos isso com a linha `imagens = []` antes do `setup()` que cria uma lista vazia e aponta o nome `imagens` para ela.

Usaremos a função `sketch_path()` do py5, com o argumento `'data'` para obter o caminho da pasta *data* que está ao lado do seu *sketch*.

> Note que essa informação obtida do caminho da pasta no disco (path) não é um simples *string* mas um objeto especial da biblioteca padrão do Python do tipo `pathlib.Path` que sabe fazer uma porção de coisas úteis.
> 
> - Sabe listar os itens nele contidos, se for uma pasta com`p.iterdir()`, entregando objetos `pathlib.Path` para cada um deles.
> - Sabe informar se é um arquivo (e não pasta/sub-pasta) com `p.is_file()`
> - Não vamos usar aqui, mas é possível juntar um nome de arquivo ou de uma sub-pasta com o path da pasta mãe, formando o "caminho completo" do item: 
>  ```python
>   caminho_imagem = sketch_path('data')  / 'uma_imagem.png'  # um novo pathlib.Path que aponta para a imagem
>  ```
> Isso pode ser importante saber no futuro pois em diferentes sistemas operacionais os strings que representam o caminho para um arquivo ou pasta usam símbolos diferentes como separadores em cada sistema, melhor deixar o Python fazer a junção para você!

Depois do procedimento que popula a lista `caminhos_arquivos`, que contém o caminho completo para os arquivos de imagem, nós vamos pegar cada um desses caminhos e usá-lo para carregar os dados da imagem com a função `load_image()` do py5. Essa função aceita um *string* com a localização de um arquivo no disco, mas aceita também um objeto `pathlib.Path`,e devolve um objeto `Py5Image` que pode ser mostrado na tela com a função `image()` posteriormente.

```python
from random import choice

imagens = []  # Lista que vai receber objetos Py5Image (Processing Image data)

def setup():
    size(400, 400)
    # Path da pasta data, não use antes do setup!
    data_folder = sketch_path('data')  # este é um objeto pathlib.Path
    # Ponha as imagens na pasta /data/ ao lado do seu sketch
    # Começa olhando para os itens da pasta, confere se é uma imagem e
    # se for, guarda na lista caminhos_arquivos.
    caminhos_arquivos = []
    # Repare que .iterdir() e .is_file() são métodos dos objetos pathlib.Path
    # .iterdir() entrega Path dos seus itens, mas vai crashar se pasta não existir
    for caminho_arquivo in data_folder.iterdir():  
        if caminho_arquivo.is_file() and has_image_ext(caminho_arquivo.name):
            caminhos_arquivos.append(caminho_arquivo)
    # Agora efetivamente carrega na memória cada imagem a partir dos caminhos
    # listados no passo anterior. Se alista estiver vazia não faz nada.
    for caminho_arquivo in caminhos_arquivos:
        img = load_image(caminho_arquivo)
        imagens.append(img)
    # Vamos congelar a repetição do draw() com no_loop().
    no_loop()  
    # Clique com o mouse para uma nova imagem, redraw() na função mouse_clicked()
        
def draw():
    background(0)
    random_image = choice(imagens)
    # Para encolher proporcionalmente a imagem caso ela não caiba na àrea de desenho
    fator_escala = 1 # caso a imagem caiba perfeitamente
    # se a largura da imagem for maior que a largura da àrea de desenho
    if random_image.width > width:  
        fator_escala = width / random_image.width
    # se mesmo tento sido já reduzida, a altura não couber
    if random_image.height * fator_escala > height:  
        fator_escala = height / random_image.height
    # Mostra a imagem centrada na àrea de desenho
    image_mode(CENTER)
    image(random_image, width / 2, height / 2,
          random_image.width * fator_escala, random_image.height * fator_escala)
                     
def mouse_clicked():  # executada quando o mouse é clicado
    redraw()          # pede para executar mais um ciclo da função draw()
    
def has_image_ext(file_name):
    """
    Responde se a extensão do arquivo está na tupla contendo
    extensões válidas para imagens.
    """
    valid_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
    file_ext = file_name.split('.')[-1]
    return file_ext.lower() in valid_ext

```
### Uma versão que checa se a pasta existe e não dá erro se a pasta estiver vazia

<details>
  <summary>clique para ver</summary>

<code>

    from random import choice

    imagens = []  # Lista que vai receber objetos Py5Image (Processing Image data)

    def setup():
        size(400, 400)
        data_folder = sketch_path('data')  # este é um objeto pathlib.Path
        caminhos_arquivos = []
        try:
            for caminho_arquivo in data_folder.iterdir():  
                if caminho_arquivo.is_file() and has_image_ext(caminho_arquivo.name):
                    caminhos_arquivos.append(caminho_arquivo)
        except OSError as e:
            print(e)
            # Exemplo: [Errno 2] Arquivo ou diretório inexistente: '~/exemplos/data'

        # Agora efetivamente carrega na memória cada imagem a partir dos caminhos
        # listados no passo anterior. Se alista estiver vazia não faz nada.
        for caminho_arquivo in caminhos_arquivos:
            img = load_image(caminho_arquivo)
            imagens.append(img)
        # Vamos congelar a repetição do draw() com no_loop().
        no_loop()  
        # Clique com o mouse para uma nova imagem, redraw() na função mouse_clicked()

    def draw():
        background(0)
        if imagens:
            random_image = choice(imagens)
        else:
            random_image = create_graphics(400, 400)
            random_image.begin_draw()
            random_image.text_size(20)
            random_image.text('Imagens não encontradas', 100, 100)
            random_image.end_draw()
        # Para encolher proporcionalmente a imagem caso ela não caiba na àrea de desenho
        fator_escala = 1 # caso a imagem caiba perfeitamente
        # se a largura da imagem for maior que a largura da àrea de desenho
        if random_image.width > width:  
            fator_escala = width / random_image.width
        # se mesmo tento sido já reduzida, a altura não couber
        if random_image.height * fator_escala > height:  
            fator_escala = height / random_image.height
        # Mostra a imagem centrada na àrea de desenho
        image_mode(CENTER)
        image(random_image, width / 2, height / 2,
              random_image.width * fator_escala, random_image.height * fator_escala)

    def mouse_clicked():  # executada quando o mouse é clicado
        redraw()          # pede para executar mais um ciclo da função draw()

    def has_image_ext(file_name):
        """
        Responde se a extensão do arquivo está na tupla contendo
        extensões válidas para imagens.
        """
        valid_ext = ('jpg', 'png', 'jpeg', 'gif', 'tif', 'tga')
        file_ext = file_name.split('.')[-1]
        return file_ext.lower() in valid_ext

</code>

</details>

## Assuntos relacionados

- Estrutura de pixels das imagens em [Pixels e imagens](pixels.md)
- [Lendo e escrevendo texto em arquivos (*file IO*)](file_IO.md)
- [Lendo todas as imagens de uma pasta selecionada pela pessoa usuária](imagens_externas_pasta.md)
