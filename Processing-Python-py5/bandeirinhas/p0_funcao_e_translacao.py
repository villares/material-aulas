"""
Exemplo de declaração de uma função com parâmetros; translação do sistema de cordenadas,
preservando o sistema orginal numa pilha com push_matrix() e chamada da nova função.
Nota: A área de desenho padrão do py5 é 100 x 100 pixels, com um fundo cinza.
"""


def setup():
    """ Código chamado uma vez no início da execução pelo Processing """
    size(100, 100)  # define as dimensões da área de desenho
    bandeirinha(50, 50)  # chama a função bandeirinha


def bandeirinha(px, py, tamanho=50):
    """ Desenha polígono em torno das coordenadas passadas, com tamanho padrão 50 """
    metade = tamanho / 2
    with push_matrix():   # preseservando o sistema de coordenadas anterior,
        translate(px, py)  # translada o sistema de coordenadas
        begin_shape()  # inicia polígono
        vertex(-metade, -metade)
        vertex(-metade, metade)
        vertex(0, 0)
        vertex(metade, metade)
        vertex(metade, -metade)
        end_shape(CLOSE)  # encerra polígono, fechando no primeiro vértice
