# size(200, 200)
# scale(2)
rect(20, 10, 40, 80)     # retângulo (x, y, largura, altura)
ellipse(10, 20, 50, 80)  # oval (x, y, largura, altura)
line(10, 10, 50, 50)     # linha do ponto 1 ao ponto 2 (x1, y1, x2, y2)
point(40, 50)            # ponto em x:40 y:50
square(55, 30, 40)       # quadrado na posição x:55 y:30 e lado:40
circle(50, 100, 40)      # círculo na posição x:50 y:100 e diâmetro:40

from pathlib import Path
p = Path.cwd().parent / 'Processing-Python-py5' / 'assets' / '01-formas.png'
save(p)