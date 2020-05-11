## Um botão simples


Aqui um exemplo de um botão muito simplificado, basicamente uma função que desenha um retângulo com texto e retorna `True` caso o mouse esteja apertado sobre ele (e `False` caso contrário).

```python
fundo = color(0)

def setup():
    size(400, 400)

def draw():
    background(fundo)
    global fundo
    
    if botao_simples(100, 100, 200, 50, "vermelho"):
        fundo = color(255, 0, 0)

    if botao_simples(100, 250, 200, 50, "preto"):
        fundo = color(0)

def botao_simples(x, y, w, h, _text):
    mouse_over = (x < mouseX < x + w and
                  y < mouseY < y + h)
    if mouse_over:
        fill(140)
    else:
        fill(240)
    rect(x, y, w, h, 5)
    fill(0)
    textAlign(CENTER, CENTER)
    text(_text, x + w / 2, y + h / 2)
    # Boão devolve verdadeiro se estiver com o mouse apertado sobre ele
    if mouse_over and mousePressed:
        return True
    else:
        return False
 ```
    
Repare que o comportamento deixa um pouco a desejar em relação a um botão apresentado pela interface do sistema operacional ou em um site. Esse botão que vimos é acionado no momento do pressionar do botão do mouse, os botões tradicionais são acionados no momento em que o botão do mouse é solto, completando um 'clique'.
    
É possível obter um comportamento semelhante de acionamento com um clique completo repetindo a chamada dos botões, uma vez em `draw()` para visualização e outra na função de evento `mouseClicked()`, como no código abaixo:
    
```python
fundo = color(0)

def setup():
    size(400, 400)

def draw():
    background(fundo)
    # desenha os botões mas ignora o resultado
    botao_clique(100, 100, 200, 50, "vermelho")
    botao_clique(100, 250, 200, 50, "preto")

def mouseClicked():
    global fundo
    # confere clique na posição do botão vermelho
    if botao_clique(100, 100, 200, 50, "vermelho"): 
        fundo = color(255, 0, 0)
    # confere clique na posição do botão preto
    if botao_clique(100, 250, 200, 50, "preto"): 
        fundo = color(0)
                        
def botao_clique(x, y, w, h, _text):
    mouse_over = (x < mouseX < x + w and
                  y < mouseY < y + h)
    if mouse_over:
        fill(140)
    else:
        fill(240)
    rect(x, y, w, h, 5)
    fill(0)
    textAlign(CENTER, CENTER)
    text(_text, x + w / 2, y + h / 2)
    # Alterado! Agora devolve verdadeiro só com mouse_over
    if mouse_over:
        return True
    else:
        return False
```
    
