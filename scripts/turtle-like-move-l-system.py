

def setup():
    size(400, 400)
    translate(200, 350)  # move a origem para um ponto mais abaixo do que o meio da tela
    text('0', 0, 0)
    
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final da linha
    text('1', 0, 0)

 
    rotate(radians(45))  # gira o papel 45 graus
    
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final dalinha

    push_matrix()        # guarda o sistema de coordenadas (1)
    
    rotate(radians(45))  # "gira o papel" 45 graus para a esquerda
    
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final dalinha
    
    pop_matrix()         # vota ao sistema de coordenadas (1)
    
    rotate(radians(-45))  # "gira o papel" 45 graus para a direita
        
    line(0, 0, 0, -100)  # uma linha de tamanho 100 para cima
    translate(0, -100)   # muda a origem para o final dalinha
    