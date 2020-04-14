# Laço de repetição `while`

Os laços de repetição baseados no `while` tem a seguinte estrutura:

```python
while condição: #  enquanto a 'condição' for verdadeira, execute:
    corpo 
```
No código do corpo é em geral necessário atualizar algum elemento da condição avaliada pelo laço, para que ela se torne falsa em algum momento, ou então invocar `break` de forma a evitar a repetição infinita.

Um exemplo de uso do laço `while` em que um ângulo `ang` vai tendo o seu valor aumentado (`ang += passo`) até que deixa de ser menor que 360 graus (em radianos, a constante Pi vezes dois, ou, no Processing `TWO_PI`) dessa forma encerrando o laço (e o desenho dos pontos de uma estrela). 

```pyde
def setup():
    size(400, 400)
    background(0)
    estrela(width / 2, height / 2, 190, 100, 10)
def estrela(x, y, raio_a, raio_b, num_pontas):
    passo = TWO_PI / num_pontas
    beginShape()
    ang = 0
    while ang < TWO_PI:  # enquanto o ângulo for menor que 2 * PI:
        sx = cos(ang) * raio_a
        sy = sin(ang) * raio_a
        vertex(x + sx, y + sy)
        sx = cos(ang + passo / 2.) * raio_b
        sy = sin(ang + passo / 2.) * raio_b
        vertex(x + sx, y + sy)
        ang += passo  # aumente o ângulo um passo
    endShape(CLOSE)
```

![estrela](https://raw.githubusercontent.com/villares/material-aulas/master/Processing-Python/assets/estrela.png)
