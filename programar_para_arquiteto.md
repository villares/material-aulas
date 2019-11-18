## Introducao à programação 

Entender como fracionar os objetos, o que vem na frente e o que vem atrás, como eles sao formados e como se comportam separadamente, para depois entender o conjunto final. Como arquitetos expressamos usualmente o pensamento por meio do desenho adotamos como plano de fundo deste desenho, geralmente, um plano cartesiano onde vamos interligando os pontos por meio de linhas ate formar a perspectiva final. 

Por aqui, na programação e como se estivessemos fazendo a mesma coisa so que narrando e detalhando o passo a passo do que vamos desenhar.  Primeiro desenhamos os poligonos que vao por baixo por meio de coordenadas no plano cartesiano depois desenhamos os poligonos que vao por cima da mesma forma de coordenadas. Feito isso, voce pode ir trabalhando de diversas formas: mover algo, escalonar, repetir ...

E para ir programando (escrevendo) voce pode consultar uma espécie de dicionario, a [referência](https://py.processing.org/reference).

### Olho - exemplo de aplicação

Especificar o tamanho da tela que iremos desenhar. Desenhar uma elipse de tamanho determinado, detalhamos sua altura e largura por meio de coordenadas no plano cartesiano que também, por consequência, irá mostrar onde essa elipse estara. Em seguida, vamos desenhar o interior do olho, que em desenho fica por cima da elipse branca por meio de um circulo de cor a escolher (colocar a cor é só você digitar fill e escrever os parâmetros RGB dela).

```python
# exemplo olho 
def setup():
    size(600, 400)
    background(0)
    olho(300, 100, random(50, 100)) # x, y, tamanho sorteado
    olho(100, 200, random(10, 150)) 
    olho(200, 300, random(10, 150))
    
def olho(x, y, tamanho) :
    """Olho precisa de 3 parâmetros"""
    noStroke()
    fill(255)
    ellipse(x, y, tamanho, tamanho/2)
    fill(0)
    circle(x, y, tamanho*.40)
```
