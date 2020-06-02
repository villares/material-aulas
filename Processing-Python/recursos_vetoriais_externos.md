# Como usar recursos vetoriais externos

## Carregando um arquivo SVG com `loadShape()`

![](assets/bot1.svg)

>arquivo: [bot1.svg](assets/bot1.svg)

Podemos carregar (*load*) na memória dados de arquivos vetoriais externos nos formatos SVG e OBJ. Para isso usamos a função `loadShape()`, mas é preciso indicar onde está o arquivo (o chamado 'caminho completo' do arquivo), ou que ele esteja na pasta `/data/` dentro da pasta do seu *sketch* (programa).

```
sketch_2020_04a                (pasta/folder do sketch)
  L  sketch_2020_04a.pyde      (arquivo com o código)
  L  data                      (pasta/folder)
       L  bot1.svg          (arquivo svg)
```

Note que a operação de carregar o arquivo é relativamente demorada e nunca deve ser executada dentro do laço `draw()`. Em geral só precisamos carregar uma vez e fazemos isso no `setup()`. Também é comum criarmos uma variável global que faz referência aos recurso vetoriais carregados, neste exemplo a variável `svg`:

```pyde
def setup():
    size(400, 400)
    global svg
    svg = loadShape("bot1.svg")  # arquivo SVG na pasta /data/

def draw():
    # shape(svg, x, y) desenha o arquivo no tamanho original
    shape(svg, 100, 100) 
    # shape(svg, x, y, largura, altura) força um tamanho
    # svg.width e svg.height apontam as dimensões do arquivo original
    # podemos mostrar o recurso com metade da sua largura e altura originais assim:
    shape(svg, 0, 0, svg.width / 2, svg.height / 2)
```

![](assets/bot1.png)

Os objetos `PShape`, que armazenam os dados vetoriais, tem uma série de métodos (funções internas desses objetos) que podem ser consultados na referência do [Processing modo Java / PShape](https://processing.org/reference/PShape.html). A página da referência do Processing modo Python está incompleta mas os métodos de *PShape* são os mesmos.

### Assuntos relacionados

- [Carregando imagens externas](imagens_externas.md)
- [Exportando SVG](exportando_svg.md)
- Para carregar objetos 3D no formato OBJ, consulte a página sobre [P3D](https://github.com/villares/material-aulas/blob/master/Processing-Python/desenho-3D.md)
