from py5_tools import animated_gif

tamanho = 50

def setup():
    """Código de configuração, executado no início pelo py5."""
    global x, y     # a instrução global permite atribuir nomes a variáveis globais nesta função
    size(100, 100)  # área de desenho
    x, y = width / 2, height / 2   # coordenadas do meio da área de desenho
    animated_gif('particulas0.gif', count=22, period=0.10, duration=0.10)
    

def draw():
    """O laço principal de repetição do Processing usado para animações e sketches interativos."""
    global x, y
    background(0)  # limpeza do frame, fundo preto
    circle(x, y, tamanho)  # desenha um círculo
    x += 1  # incrementa o x (equivale a x = x + 1)
    y += 1  # incrementa o y
    if x > width + tamanho / 2:
        x = -tamanho / 2
    if y > height + tamanho / 2:
        y = -tamanho / 2