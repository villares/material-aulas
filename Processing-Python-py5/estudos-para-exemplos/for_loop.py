
size(400, 400)

no_fill()  # formas sem preenchimento

cores = [
    color(0, 0, 200),    # azul
    color(255, 255, 0),  # amarelo
    color(0, 128, 0),    # verde
    color(255, 0, 255),  # magenta
    color(0, 255, 255),  # ciano
    ]
x = 40
for c in cores:
    fill(c)
    rect(x, 40, 64, 320)
    x = x + 64
    
save('for_c_in_cores.png')
           
# size(400, 400)
# diâmetros = [300, 250, 200, 150, 100, 50]  # uma lista de números
# for d in diâmetros:  # atribua a variável `d` para cada diâmetro
#     circle(200, 200, d)  # desenha a cada volta um círculo o diâmetro `d` da vez
#     
#     
# save('for_circulos.png')