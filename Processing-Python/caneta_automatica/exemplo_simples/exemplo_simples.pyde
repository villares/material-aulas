from caneta_automatica import *

def setup():
    size(400, 400)
    inicie_caneta()
    quadrado(100)  # chama a função quadrado
    
    # saveFrame("quadrado.png")

def quadrado(tamanho):
    for i in range(4):  # repete 4 vezes: 
        ande(tamanho)   # anda e faz uma linha
        vire(90)        # viar 90 graus à esquerda
        
