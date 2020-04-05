# Tipografia

## Trabalhando com fontes e texto no Processing

Usamos `text("Lorem Ipsum dolor", x, y)` para escrever um texto na área de desenho. O tamanho pode ser controlado, em pontos, por `textSize()`. O alinhamento pode ser alterado por `textAlign()`. A cor vem do `fill()`.

### Exemplo básico

```pyde
"""
Adaptado do tutorial
https://py.processing.org/tutorials/typography/
"""

x = 33
y = 60

def setup() :
    size(100, 100)
    textSize(12)
    textAlign(CENTER, BOTTOM) # pode ser usado LEFT, RIGHT no primeiro parâmetro e CENTER ou TOP no segundo
    noStroke()

def draw() :
    fill(204, 120)
    rect(0, 0, width, height)
    fill(0)
    # Se o mouse estiver sobre o texto, mova!
    if ((mouseX >= x) and (mouseX <= x+55) and
        (mouseY >= y-24) and (mouseY <= y)) :
        x += random(-2, 2)
        y += random(-2, 2)
    
    text(u"Cócegas", x, y)
```

## Definindo a fonte

Se não indicarmos alguma, uma fonte padrão será usada, mas podemos criar uma nova fonte (PFont) e usar em `textFont()`,
a partir de uma fonte já instalada ou de um arquivo vetorial **.ttf** ou **.otf** na pasta *"""data**:

```pyde
# para ver as fontes instaladas no seu computador
for font_name in PFont.list():
    print(font_name)
# para usar a fonte Vera Sans Mono no estilo negrito
f = createFont("Bitstream Vera Sans Mono Bold", 24)
textFont(f)
```

Especialmente no caso de não termos permissão para distribuir o arquivo vetorial da fonte, podemos criar uma fonte bitmap
a partir da original e distribuir este novo arquivo **.vlw**, na pasta *"""data**.
Usando a ferramenta **Tool > Create Font...**  produzimos o arquivo da fonte que pode ser carregado da seguinte maneira:

```pyde
font = loadFont("LetterGothicStd-32.vlw")
```

## Uma grade de letras, símbolos, glifos!

![grade](https://raw.githubusercontent.com/arteprog/programacao-criativa/master/assets/imagens/typogrid.png)

Copie o arquivo descompactado **.otf*** da fonte [Garoa Hacker Clube Bold](https://garoa.net.br/wiki/Fonte_Garoa_Hacker_Clube_Bold) na sub-pasta *"""data** do seu sketch.

```pyde

```

## Bibliografia

REAS, C. FRY, B. Processing: a programming handbook for visual designers and artists. Cambridge, Mass: MIT Press, 2007. 
