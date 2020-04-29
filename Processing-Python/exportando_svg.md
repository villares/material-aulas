# Exportando SVG

Muito semelhante a exportação de PDF, para salvar um arquivo vetorial SVG, é necessário adicionar uma biblioteca de exportação, que já vem com o Processing, acrescentando esta linha no início do *sketch*:

``` python
add_library('svg')
```
Isso pode ser feito manualmente ou pelo menu *Sketch* do Processing IDE:
***Sketch > Importar Biblioteca > SVG Export***

#### Usando um objeto PGraphics 

A estratégia mostrada a seguir permite mostrar na tela o desenho mas salvar um arquivo ajustes especiais, como por exemplo dimensões escaladas.

```python
"""
Tecle 'e' para salvar um único frame e encerrar o sketch
"""

add_library('svg')

save_frame = False
fator_escala = 3.78 # 500px -> 1890px ~ 500mm

def setup():
    global svg_output
    size(500, 500)
    svg_output = createGraphics(int(width * fator_escala),
                                int(height * fator_escala),
                                SVG, "arquivo.svg")

def draw():
    if save_frame:
        beginRecord(svg_output)
        svg_output.strokeWeight(.33)  # linha mais fina ainda!
        svg_output.scale(fator_escala)
        svg_output.background(200)  # sem background fica fundo transparente
        
    # desenho aqui, sai na tela e no arquivo
    rect(100, 100, 100, 100)  

    if save_frame:
        endRecord()  # encerra a gravação do arquivo
        exit()  # encerra o sketch

def keyPressed():
    global save_frame
    if key == 'e':
        save_frame = True

```

### Assuntos relacionados:

- [Exportando PDF](exportando_pdf.md)

````

````