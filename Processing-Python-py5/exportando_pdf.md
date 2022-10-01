# Exportando PDF

Saver salvar um PDF é muito útil, pois é formato que preserva informação vetorial, de maneira semelhante ao SVG(recomendo a leitura da página sobre exportar SVG também).

É importante considerar que existe mais de uma estratégia para exportar arquivos vetorias. Imagens *raster* são mais fáceis, basta exportar o que acumulou na tela em qualquer momento, com desenho vetorial ou você redesenha tudo a cada quadro ou você tem que pensar com cuidado sobre a acumulação de quadros para o arquivo não ficar imenso. Vocẽ tem interação? Precisa ligar e desligar a gravação dos frames.

Veja nos exemplos abaixo as llinhas de código que você precisa acrescentar ao longo so seu *sketch*, dependendo do que quer exportar.

# PDF simples

# Salvando um frame único do `draw()`, sem acumulação

A estratégia a seguir permite a interatividade, com o uso de `draw()`, mas exige que desenho seja realizado inteiro em cada frame.

```python
salvar_pdf = False  # um indicador ('flag') dispara a exportação


def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)


def draw():
    global salvar_pdf  # necessário para desligar o 'flag'
    if salvar_pdf:     # inicia a gravação
        begin_record(PDF, "####.pdf")

    # Aqui vai o desenho a ser gravado
    random_seed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)

    if salvar_pdf:    # se verdadeiro, gravação em curso
        end_record()   # termina a gravação
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
        push_matrix()
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * reducao - random(0, 2))
        rotate(-ang * 2)
        galho(tamanho * reducao - random(0, 2))
        pop_matrix()


def key_pressed():
    global seed, salvar_pdf  # variáveis globais que serão modificadas
    if key == " ":
        seed = int(random(100000))
        print(seed)
    if key == "p":  # aciona o 'flag' de gravação do PDF
        salvar_pdf = True
        print("salvando PDF")


```

[Exemplo de PDF com um frame](assets/exemplo.pdf)

# Salvando a acumulação na tela de vários frames

Não é possível capturar diretamente o produto da acumulação do desenho na tela, como acontece com a exportação de uma imagem raster que fazemos usando `saveFrame()`, mas é possível gravar o PDF durante vários frames, acumulando os desenhos produzidos no arquivo e na tela ao mesmo tempo. Neste exemplo você  'liga' e 'desliga'  a gravação de frames no PDF usando a tecla 'p'.

```python


gravando_pdf = False  # 'flag'/indicador de gravação do PDF


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


def key_pressed():
    global gravando_pdf
    if key == "p":                        # A tecla 'p' muda o 'flag' de gravação do PDF
        gravando_pdf = not gravando_pdf   # alternando o seu estado entre True e False
        if gravando_pdf:
            begin_record(PDF, "####.pdf")  # inicia a gravação do PDF
            background(0)                 # sem isso, fundo branco...
            print(u"iniciando gravação de PDF: {:04n}".format(frame_count))
        else:
            end_record()                   # encerra a gravação do PDF
            print(u"encerrando gravação de PDF")


```
[Exemplo de PDF com vários frames](assets/exemplo2.pdf)


Um segundo exemplo de salvar com acumulação de frames

```python


gravando_pdf = False


def setup():
    size(600, 600)
    fundo()


def fundo():
    background(255)
    filas = colunas = 12
    tam = width / colunas
    for j in range(filas):
        for i in range(colunas):
            fill(0)
            circle(i * tam + tam / 2, j * tam + tam / 2, tam)


def draw():
    if mouse_pressed and (mouse_x, mouse_y) != (pmouse_x, mouse_y):
        fill(255)
        no_stroke()
        meu_triangulo(mouse_x, mouse_y, 50)


def meu_triangulo(x, y, tam):
    triangle(x - tam / 2, y + tam / 3,
             x + tam / 2, y + tam / 3,
             x, y - tam / 3)


def key_pressed():
    global gravando_pdf
    if key == 'g':
        if not gravando_pdf:     # if gravando_pdf == False
            gravando_pdf = True
            begin_record(PDF, 'desenho####.pdf')
            fundo()
            print(u'Gravação iniciada')
        else:  # quando gravando == True
            gravando_pdf = False
            end_record()
            print(u'Gravação encerrada')


```


# Outras estratégias

# Usando um objeto PGraphics

Usando `create_graphics()` podemos mostrar na tela o desenho mas salvar o arquivo do desenho com alguns ajustes especiais.

```python

f = create_graphics(width * 2, height * 2, PDF, "file.pdf")
begin_record(f)  # inicia a gravação do arquivo
f.strokeWeight(2)
f.scale(2)
# o seu desenho vai aqui

# encerra a gravação
end_record()
```
Veja um exemplo mais completo desta estratégia no exemplo a seguir, que produz um PDF com várias páginas.

# Salvando um PDF com múltiplas páginas

```python


nome_arquivo = "10_paginas.pdf"


def setup():
    global pdf
    size(300, 400)
    pdf = create_graphics(width * 2, height * 2, PDF, nome_arquivo)
    begin_record(pdf)  # inicia a gravação do arquivo
    pdf.scale(2)


def draw():
    background(200, 200, 240)
    t = random(50, 100)
    x, y = random(t, width - t), random(t, height - t)
    ellipse(x, y, t * 2, t * 2)

    if frameCount == 10:
        end_record()
        exit()
    else:
        pdf.next_page()


```

# Limitações

O que não funciona quando exportamos em PDF?

- A chamada `blend_mode(MULTIPLY)` ou qualquer outra variante de `blend_mode()` não tem efeito no PDF(só na tela).

- Para exportar desenhos em 3D, é preciso usar `begin_raw()`  e `end_raw()` em lugar de `begin_record/end_record` e o resultado é um tanto deficiente(veja exemplo em[Exportando SVG](exportando_svg.md)).

# O que pode dar errado? Algumas considerações finais

Se não estiver funcionando, confira se não está esquecendo algo sobre exportação de PDF:

- Pense com cuidado se seu sketch precisa salvar apenas um frame ou acumular frames(muda a estratégia um pouco)
- Não esqueça que só aparecem na gravação ações e ajustes feitos depois do begin_record() ou beginRaw() e isso é bastante crítico em relação a:
    - `background()`
    - ajustes como `colorMode()`, `rectMode()` ou outros ajustes de atributos
- não esqueça de declarar com `global` o flag/indicador tanto no `draw()` como no `key_pressed()`, se apropriado, para alterar o estado ou início da gravação.

# Assuntos relacionados:

- [Exportando SVG](exportando_svg.md)
