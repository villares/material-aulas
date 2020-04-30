# Exportando PDF

Para  salvar um PDF, formato que preserva informação vetorial, de maneira semelhante ao SVG, é necessário adicionar uma biblioteca de exportação que já vem com o Processing, acrescentando esta linha no início do *sketch*:

``` python
add_library('pdf')
```
Isso pode ser feito manualmente ou pelo menu * Sketch* do Processing IDE:
***Sketch > Importar Biblioteca > PDF Export***

![adicionando](assets/pdf_export.png)

Veja nos exemplos abaixo as llinhas de código que você precisa acrescentar ao longo so seu *sketch*, dependendo do que quer exportar.

##  PDF simples

### com acumulação no canvas de vários frames

Não é possível capturar diretamente o produto da acumulação do desenho na tela, como acontece com a exportação de uma imagem raster que fazemos usando `saveFrame()`, mas é possível gravar o PDF durante vários frames, acumulando os desenhos produzidos no arquivo e na tela ao mesmo temo. Neste exemplo você  'liga' e 'desliga'  a gravação de frames no PDF usando a tecla 'p'.        

```python
add_library('pdf')

gravando_pdf = False  # indica a gravação do PDF

def setup():
    size(500, 500)
    background(0)

def draw():
    colorMode(HSB)    # se puser ajustes no setup não entram na gravação!
    rectMode(CENTER)  # fazendo o PDF ficar diferente do resultado na tela
    if mousePressed:
        fill(random(255), 200, 200, 100)
        rect(mouseX, mouseY, 50, 50)

    if not gravando_pdf:
        textSize(18)
        fill(255)
        text(u"Não está gravando o PDF\n" + 
             u"aperte 'p' para começar e parar a gravação",
             20, 20)

def keyPressed():
    global gravando_pdf 
    if key == "p":  # A tecla 'p' aciona o 'flag' de gravação do PDF
        gravando_pdf = not gravando_pdf    
        if gravando_pdf:
            beginRecord(PDF, "####.pdf")  # inicia a gravação do PDF
            background(0) # sem isto, fundo branco... 
            print(u"iniciando gravação de PDF: {:04n}".format(frameCount))
        else:
            endRecord()   # termina a gravação
            print(u"encerrando gravação de PDF")
```
[Exemplo de PDF com vários frames](assets/exemplo2.pdf)


###  salvando frame único do `draw()`, sem acumulação

A estratégia a seguir também permite a interatividade, com o uso de `draw()`, mas exige que desenho seja realizado inteiro em cada frame.

```python
add_library('pdf')

salvar_pdf = False  # um indicador ('flag') dispara a exportação

def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)

def draw():
    global salvar_pdf  # necessário para desligar o 'flag'
    if salvar_pdf:     # inicia a gravação 
        beginRecord(PDF, "####.pdf")         
        
    # Aqui vai o desenho a ser gravado
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)

    if salvar_pdf:    # se verdadeiro, gravação em curso
        endRecord()   # termina a gravação
        salvar_pdf = False  # desliga o 'flag'

def galho(tamanho):
    """
    função recursiva que desenha galhos
    """
    ang = radians(mouseX)
    reducao = .8
    strokeWeight(tamanho / 10)
    line(0, 0, 0, -tamanho)
    if tamanho > 5:
        pushMatrix()
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * reducao - random(0, 2))
        rotate(-ang * 2)
        galho(tamanho * reducao - random(0, 2))
        popMatrix()

def keyPressed():
    global seed, salvar_pdf  # variáveis globais que serão modificadas
    if key == " ":
        seed = int(random(100000))
        print(seed)
    if key == "p":  # aciona o 'flag' de gravação do PDF
        salvar_pdf = True
        print("salvando PDF")
```

[Exemplo de PDF com um frame](assets/exemplo.pdf)

## Outras estratégias

### usando um objeto PGraphics

Usando `createGraphics()` podemos mostrar na tela o desenho mas salvar o arquivo do desenho com alguns ajustes especiais. 

```python
add_library('pdf')
f = createGraphics(width * 2, height * 2, PDF, "file.pdf")
beginRecord(f)  # inicia a gravação do arquivo
f.strokeWeight(2)
f.scale(2)
# o seu desenho vai aqui

# encerra a gravação
endRecord()  
```
Veja um exemplo mais completo desta estratégia em [Exportando SVG](exportando_svg.md).

### PDF com  múltiplas páginas

```python
add_library('pdf')

nome_arquivo = "10_paginas.pdf"

def setup():
    global pdf
    size(300, 400)
    pdf = createGraphics(width * 2, height * 2, PDF, nome_arquivo)
    beginRecord(pdf)  # inicia a gravação do arquivo
    pdf.scale(2)

def draw():
    background(200, 200, 240)
    t = random(50, 100)
    x, y = random(t, width - t), random(t, height - t)
    ellipse(x, y, t * 2, t * 2)        
    
    if frameCount == 10:
        endRecord()
        exit()
    else:
        pdf.nextPage()
```     
        
## Limitações

O que não funciona quando exportamos em PDF?

- blendMode(MULTIPLY)ou qualquer outra variante de blendMode() não tem efeito no PDF (só na tela).

- Para exportar desenhos em 3D, é preciso usar `beginRaw()`  e `endRaw()`  em vez de `beginRecord/endRecord` e o resultado é deficiente (veja em [Exportando SVG](exportando_svg.md)).

### Assuntos relacionados:

- [Exportando SVG](exportando_svg.md)
