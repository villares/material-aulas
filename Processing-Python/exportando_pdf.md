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

<object data="assets/exemplo2.pdf" type="application/pdf" width="500px" height="500px">
    <embed src="assets/exemplo2.pdf">
        <p>Este browser não lê PDFs. Você pode baixá-lo aqui: <a href="assets/exemplo2.pdf">PDF exemplo</a>.</p>
    </embed>
</object>

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
###  salvando frame único do `draw()`, sem acumulação

Esta estratégia também permite  a interatividade, com o uso de `draw()`, mas exige que desenho que seja realizado (reconstruído) todo em cada frame.

<object data="assets/exemplo.pdf" type="application/pdf" width="500px" height="500px">
    <embed src="assets/exemplo.pdf">
        <p>Este browser não lê PDFs. Você pode baixá-lo aqui: <a href="assets/exemplo.pdf">PDF exemplo</a>.</p>
    </embed>
</object>

```python
add_library('pdf')

salvar_pdf = False  # um 'flag' para disparar a exportação

def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)

def draw():
    global salvar_pdf  # necessário para desligar o 'flag'
    if salvar_pdf: # inicia a gravação 
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
    if key == "p":  # A tecla 'p' aciona o 'flag' de gravação do PDF
        salvar_pdf = True
        print("salvando PDF")
```

## Outras estratégias

### Usando um objeto PGraphics

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

## Múltiplas páginas

 `TO DO: Múltiplas páginas `


### Limitações

  `TO DO:  O que não funciona no PDF?`  


### Assuntos relacionados:

- [Exportando SVG](exportando_svg.md)

