# Salvando em PDF

## Adicionando a Biblioteca

Para poder salvar uma imagem vetorial em PDF, é necessário adicionar uma biblioteca de exportação, que já vem com o Processing, acrescentando esta linha no início do *sketch*:

``` phython
add_library('pdf')
```
Esta linha pode ser acrescentada manualmente ou automaticamente usando o seguinte comando do IDE:

**Menu Sketch > Importar Biblioteca > PDF Export**
![adicionando](https://github.com/zehasni/material-aulas/blob/master/ADDP_BA_2019/Adicionando_biblioteca.png?raw=true)

Também é preciso acrescentar algumas linhas de código ao longo so seu *sketch*, como no exemplo abaixo.

## Exemplo de exportação em PDF de um único frame

```
add_library('pdf')

salvar_pdf = False  # um 'flag' (indicador) para disparar a exportação

def setup():
    global seed
    seed = int(random(1000))
    print(seed)
    size(500, 500)

def draw():
    global salvar_pdf  # vai ser necessário no final para desligar o 'flag'
    if salvar_pdf:   # só executa se for acionado este 'flag'
        beginRecord(PDF, "####.pdf")  # inicia a gravação do PDF
        
    # Aqui vai o desenho que vai ser salvo em PDF
    randomSeed(seed)
    background(240, 240, 200)
    translate(250, 300)
    galho(60)

    if salvar_pdf:    # se o 'flag' está verdadeiro, gravação em curso
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
