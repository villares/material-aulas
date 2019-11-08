# Transformação do sistema de coordenadas

## Coordenadas X, Y.

Ao iniciar um arquivo com o sistema de coordenadas padrão x, y, podemos identificar que no 
Processing o eixo X tem o seu ponto de origem (zero) situa-se na extremidade do canto superior esquerdo da tela, somando (positivo) para o lado direito.
Em relação ao eixo Y, o seu ponto de origem (zero) também situa-se na extremidade do canto superior esquerdo da tela, porém, irá somando ( postitivo) para baixo, resultando em algo como:

#################################################### IMAGEM EIXO X e Y ###########################################################
![Coordenadas X e Y](nome_da_imagem_coordenadas.JPEG)

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
Como exemplo, para transformarmos os sistemas de coordenadas, considerando um *objeto* com lados *"LADO"* e *"LADOmenor"*, podemos escrever:
```python
def objeto(x, y, LADO, LADOmenor, rot):    
    L, l = LADO / 2., LADOmenor / 2.
    pushMatrix()  # pedir para criar um novo sistema de coordenadas 
    translate(x, y) # inserir novo zero,zero de coordenadas 
```


## How to save the coordinal's system 
```python
pushMatrix() 
```
