from caneta_automatica import *

size(400, 400)
inicie_caneta()


def flor(n, tamanho):
    for passo in range(n):
        ande(tamanho)
        vire(360 / n)
        if tamanho > 5:
            flor(n, tamanho / 3)


suba_caneta()
ande(100)
esquerda()  # equivale a 'vire(90)'
baixe_caneta()

flor(5, 150)

save_frame('caneta_flor.png')
