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
fator_escala = 3.78 # 255px -> ~255mm

def setup():
    global svg_output
    size(255, 255)
    svg_output = createGraphics(int(width * fator_escala),
                                int(height * fator_escala),
                                SVG, "arquivo.svg")
def draw():
    background(200) # antes do beginRecord() não sairá no SVG
    
    if save_frame:
        beginRecord(svg_output)
        svg_output.strokeWeight(.33)  # linha mais fina ainda!
        svg_output.scale(fator_escala)
        # svg_output.background(200)  # sem background, fundo transparente no SVG
        
    # desenhando aqui, sai na tela e no arquivo
    fill(255, 0, 0, 100)
    rect(50, 50, 100, 100)  
    fill(0, mouseX , mouseY, 100)
    rect(100, 100, 100, 100)  

    if save_frame:
        endRecord()  # encerra a gravação do arquivo
        exit()  # encerra o sketch

def keyPressed():
    global save_frame
    if key == 'e':
        save_frame = True

```
---

![SVG](assets/arquivo.svg)

---



### Limitações

O que não funciona quando exportamos em SVG?

- `blendMode(MULTIPLY)`ou qualquer outra variante de `blendMode()` não tem efeito no SVG (só na tela).
- TO DO: investigar outras limitações!

### Assuntos relacionados:

- [Exportando PDF](exportando_pdf.md)

````

````