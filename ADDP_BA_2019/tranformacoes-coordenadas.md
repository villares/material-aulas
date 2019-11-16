# Transformação do sistema de coordenadas

## Coordenadas X, Y.

Ao iniciar um arquivo com o sistema de coordenadas padrão x, y, podemos identificar que no 
Processing o eixo X tem o seu ponto de origem (zero) situa-se na extremidade do canto superior esquerdo da tela, somando (positivo) para o lado direito.
Em relação ao eixo Y, o seu ponto de origem (zero) também situa-se na extremidade do canto superior esquerdo da tela, porém, irá somando ( postitivo) para baixo, resultando em algo como:

![Coordenadas X e Y](coordenadas.jpg)

## Translate.

Ao criarmos uma geometria, ou desenho, para definirmos a sua origem, é necessário desvilcularmos os pontos de origem iniciais. 
Isso porque se não alterarmos as coordenadas (zero, zero) x e y respectivamente, nossa geometria proposta estará no canto superior esquerdo:

Para isso é necessário utilizarmos o comando:
```python
translate(x,y)
```
## Como utilizar o comando Translate ?

Para alterarmos as coordenadas (utilizando o comando Translate) é necessário utilizarmos o 
```python
pushMatrix()
```
O pushMatrix é responsável por definir e salvar as coordenadas que desejamos. 
Em seguida é necessário voltarmos as coordenadas para as originais.
Sendo assim, para restaurarmos as coordenadas (originais), utilizamos o comando 
```python
pophMatrix()
```
Como exemplo, para transformarmos os sistemas de coordenadas, considerando um *objeto* com lados *"lado"* e *"lada_menor"*, podemos escrever:
```python
def objeto(x, y, lado, lado_menor, rot):    
    L, l = lado / 2., lado_menor / 2.
    pushMatrix()  # pedir para criar um novo sistema de coordenadas 
    translate(x, y) # inserir novo zero,zero de coordenadas 
```

## Exemplo prático de um triângulo  azul com novo sistema de coordenadas:
```python
def setup():
    size(520, 500)
    
def draw():
    background(255)
    fill(30, 50, 200)
    objeto(150, 250, 200, 100)
    
def objeto(x, y, lado , lado_menor):
    L, l = lado / 2, lado_menor / 2
    pushMatrix() 
    translate(x, y)
    beginShape()
    vertex(20, -70)
    vertex(14, -20)
    vertex(100, -15)
    endShape(CLOSE) 
    popMatrix() 
```

