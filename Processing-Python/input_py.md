# Input com teclado e mouse - entradas de dados

No Processing, o teclado e o mouse são duas as principais formas de entrada de dados. Em outra ocasião trataremos da leitura de arquivos e outras fontes de dados. Vejamos aqui maneiras de se obter informações sobre o movimento e cliques do mouse, assim como saber sobre as teclas sendo pressionadas no teclado. 

## 1. Variáveis de sistema 

As variáveis de sistema como `mouseX`, `mouseY`, `keyPressed`e `mousePressed` contém a todo instante informações sobre o estado do teclado e mouse. Podem ser consultadas em qualquer lugar do programa e são vistas frequentemente em condicionais dentro do bloco de `draw()`.

### Exemplo

```python
def setup():
    size(200, 200)


def draw():
    if keyPressed and keyCode == SHIFT:     # se a tecla SHIFT estiver pressonada
        strokeWeight(5)                     # # usa linha mais grossa 
        stroke(255) # com traço branco
    else:           # senão, quando tecla SHIFT não estiver pressonada
        strokeWeight(1)                     # usa linha fina grossa
        stroke(0)  # com traço preto
    

    if mousePressed:                        # Se o mouse estiver pressionado
         line(pmouseX, pmouseY, mouseX, mouseY) # Então desenha uma linha da posição anterior do mouse até a atual
                # termina o bloco (repare que no faz nada se o mouse estiver solto)

```

### Quadro das variáveis de sistema

| tipo | nome | descrição | 
| --- | --- | --- |
| int | mouseButton       |    indica qual botão do mouse foi clicado `LEFT`, `RIGHT` ou `CENTER`
| boolean | mousePressed  |    estado do mouse (`True` indica pressionado)
| int | mouseX            |    informa a posição X do mouse na tela 
| int | mouseY            |    informa a posição Y do mouse na tela
| int | pmouseX           |    informa a posição X anterior do mouse na tela
| int | pmouseY           |    informa a posição Y anterior do mouse na tela
| string | key              |    caractere da última tecla alfa-numérica pressionada, ou a constante `CODED`
| int | keyCode           |    código da última tecla não alfa-numérica, como `SHIFT`, `UP` e etc.
| boolean | keyPressed    |    indica se alguma tecla está pressionada com (`True`) 


## 2. Funções acionadas por eventos

Quando definimos funções com certos nomes especiais "encomendados", como `keyPressed()`, `mousePressed()`, ou alguma outra listada no quadro mais abaixo, elas serão executadas pelo Processing quando certos "eventos" do mouse ou do teclado acontecerem. 

No jargão do desenvolvimento de interfaces isso é chamado de "tratamento de eventos". Repare que não chamamos a função no nosso código, o Processing faz isso por nós nos "eventos" apropriados, chamando a função.

As funções precisam ser definidas fora do bloco de `draw()`, e note que a definição de `draw()` precisa existir, mesmo que vazio, para garantir a execução de um "laço principal" no Processing. 

### Exemplo com `mouseDragged()` e `keyPressed()`

<!-- [exemplo1](/assets/imagens/condicional1.png) -->

```python
def setup():
    size(200, 200)


def draw(): # é necessário um draw(), mesmo que vazio, para que exista um laço principal e funcionem os eventos
    pass
    
def mouseDragged():
    line(pmouseX, pmouseY, mouseX, mouseY) # Desenha uma linha da posição anterior do mouse até a atual


def keyPressed():          # Esta função executa uma vez quando uma tecla é pressionada
    if key == 'a':         # Se a tecla do caractere 'a' foi a última pressionada
        background(200)    # Apague a tela com um fundo cinza (só executa sob as condições acima)
    
    if keyCode == DOWN:                         # Se a seta para baixo foi precionada
        saveFrame("imagem-####.png")            # salve a imagem da tela de pintura em um arquivo PNG 
        println("salvo o frame {}.".format(frameCount))  # mostre no console o número do frame
        
```

### Exemplo de `mouseWheel(event)`

Um exemplo de uso da rodinha do mouse (mouseWheel) para controlar o desenho.

```python
tamanho = 50

def setup():
    size(500, 500)
    
def draw():
    background(200)
    if tamanho > 0:
        fill(0, 0, 200)
    else:
        fill(200, 0, 0)
    square(width / 2, height / 2, tamanho)
    
def mouseWheel(event):
    movimento_roda = event.getCount()
    global tamanho
    tamanho += movimento_roda
```

### Quadro das funções acionadas por eventos

| nome da função | descrição do evento |
| --- | --- |
| mouseReleased()   | executada quando o botão do mouse é solto depois de pressionado
| mouseWheel(event) | executada quando a rodinha do mouse é girada (deslocamento obtido com `event.getCount()`)
| mouseClicked()    | executada quando o mouse é clicado (já solto o botão)
| mouseDragged()    | executada quando o mouse é movido pressionado
| mouseMoved()      | executada quando o mouse é movido
| mousePressed()    | executada quando o botão do mouse é pressionado
| keyPressed()      | executada quando uma tecla é pressionada
| keyReleased()     | executada quando uma tecla é solta
| keyTyped()        | executada quando uma tecla alfa-numérica é digitada


---
Este material é baseado no material do curso https://arteprog.space/programacao-criativa/

---
Texto e imagens / text and images: CC BY-NC-SA 4.0; Código / code: GNU GPL v3.0 exceto onde explicitamente indicado por questões de compatibilidade.
