## Uma janela de diálogo com um campo de texto como *input*

Nas implementações mais conhecidas de Python existe uma função chamada `input()` que 'pergunta' a quem estiver executando o programa que digite um texto, que é devolvido então para o programa manipular na forma de um *string*.

O Processing modo Python não tem essa função, mas com o código a seguir podemos disparar uma janela de diálogo com um campo de texto para fazer o mesmo papel!

```python
def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
```

Vejamos então um exemplo de uso, em que um clique do mouse dispara a janela para o input textual.

![](assets/input_janela.gif)

```python
nome = "clique na janela para mudar o texto"

def setup():
    size(400, 400)
    textAlign(CENTER, CENTER)
    
def draw():
    background(0, 0, 200)
    text(nome, width / 2, height / 2)
    
def mousePressed():
    global nome
    resposta = input('escreva um novo texto')
    if resposta:
        nome = resposta
    elif resposta == "":
        println("[resposta vazia]")
    else:
        println(resposta) # se cancelada a janela exibe `None` no console

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

```

