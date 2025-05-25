#
# rect(20, 10, 40, 80)     # retângulo (x, y, largura, altura)
# ellipse(10, 20, 50, 80)  # oval (x, y, largura, altura)
# line(10, 10, 50, 50)     # linha do ponto 1 ao ponto 2 (x1, y1, x2, y2)
# point(40, 50)            # ponto em x:40 y:50
# square(55, 30, 40)       # quadrado na posição x:55 y:30 e lado:40
# circle(50, 100, 40)      # círculo na posição x:50 y:100 e diâmetro:40
#
# fill(0, 255, 0)  # preenchimento verde
# ellipse(50, 50, 50, 50)  # produz um círculo verde
# 
# from pathlib import Path
# p = Path.cwd().parent / 'Processing-Python-py5' / 'assets' / '01-verde.png'
# save(p)
#
# fill(255, 0, 0)           # cor de preenchimento vermelha
# no_stroke()         # sem traço de contorno
# square(50, 50, 40)  # produz um quadrado branco 
# no_fill()          # sem preenchimento, formas vazadas
# stroke(0, 0, 255)  # exemplo de cor do traço azul, usando RGB
# stroke_weight(10)       # espessura do traço de contorno 10 pixels
# circle(50, 50, 50)  # produz um círculo vazado com contorno verde

background(255, 255, 0)  # fundo amarelo, limpa a tela 
fill(128)
no_stroke()
square(50, 50, 40)
stroke(255)
stroke_weight(5)
no_fill()
circle(50, 50, 50)

from pathlib import Path
p = Path.cwd().parent / 'Processing-Python-py5' / 'assets' / '01-background.png'
save(p)

