# Laço de repetição `while`

Os laços de repetição baseados no `while` tem a seguinte estrutura:

```python
while cond: #  enquanto a condição 'cond' for verdadeira, execute:
    corpo 
```
No código do corpo é em geral necessário atualizar algum elemento da condição avaliada pelo laço, para que ela se torne falsa em algum momento, ou então invocar `break` de forma a evitar a repetição infinita.

No exemplo abaixo usamos o laço `while` testando se o valor de um ângulo `ang` é menor que 360 graus (em radianos, a constante Pi vezes dois, ou, no Processing `TWO_PI`).

O corpo do laço produz os vértices, que são pontos de um polígono em forma de estrela, a cada ciclo, e `ang` vai tendo o seu valor aumentado (`ang += passo`), até deixar de ser menor, dessa forma encerrando o laço.

```python
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
