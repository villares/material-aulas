def setup():
    size(600, 600)
    background(0)
    grade(0, 0, width, 4)  # width é a largura da área de desenho

def grade(x_grade, y_grade, tamanho_grade, divisoes):
    tamanho_elemento = tamanho_grade / divisoes
    for i in range(divisoes):
        x = x_grade + i * tamanho_elemento
        for j in range(divisoes):
            y = y_grade + j * tamanho_elemento
            if divisoes == 1:  # uma grade de uma divisão vira um quadrado azul
                fill(0, 0, 200)
                square(x, y, tamanho_elemento)
            elif tamanho_elemento < 20:  # desenha círculos para gradedes pequenas
                fill(0, 200, 0)
                circle(x + tamanho_elemento / 2,
                       y + tamanho_elemento / 2,
                       tamanho_elemento)
            else:  # senão, chama uma subgrade com o número de divisões "sorteadas"
                grade(x, y, tamanho_elemento, int(random(1, 5)))
