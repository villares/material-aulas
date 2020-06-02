# Como usar recursos vetoriais externos

## Acessando um arquivo com `loadShape()`


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
    (svg, 100, 100)  # é possível forçar um tamanho com shape(svg, 0, 0, 100, 100)
    # svg.width e svg.height são as dimensões do arquivo original
    # podemos mostrar o recurso com metade da sua largura e altura originais assim:
    # shape(svg, 0, 0, svg.width / 2, svg.height / 2)
 
```

### Assuntos relacionados

- [Carregando imagens externas](imagens_externas.md)
- [Exportando SVG](exportando_svg.md)
