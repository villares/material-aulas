size(200, 200)
no_fill()         # formas sem preenchimento
rect_mode(CENTER) # desenhar retângulos e quadrados pelo centro

tamanhos = [20, 40, 80, 160]
for t in tamanhos:
    square(100, 100, t)
    
save('for_t_in_tamanhos.png')
           
           