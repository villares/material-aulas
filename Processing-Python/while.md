# Laço de repetição `while`

Os laços de repetição baseados no `while` tem a seguinte estrutura:

```python
while condição_principal:
    corpo
```
No corpo é necessário atualizar um elemento da condição principal para que ela se torne falsa em algum momento, ou então invocar `break` de forma a evitar um laço infinito.

Um exemplo de usao do laço `while` em que um ângulo `ang` vai tendo o seu valor aumentado (`ang += passo`) até que não seja menor que a constante matemática `TWO_PI` (duas vezes o número Pi). 

```pyde
def setup():
    size(400, 400)
    background(0)
    estrela(width / 2, height / 2, 190, 100, 10)
def estrela(x, y, raio_a, raio_b, num_pontas):
    passo = TWO_PI / num_pontas
    beginShape()
    ang = 0
    while ang < TWO_PI:
        sx = cos(ang) * raio_a
        sy = sin(ang) * raio_a
        vertex(x + sx, y + sy)
        sx = cos(ang + passo / 2.) * raio_b
        sy = sin(ang + passo / 2.) * raio_b
        vertex(x + sx, y + sy)
        ang += passo
    endShape(CLOSE)
```

![estrela](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/estrela.png)
