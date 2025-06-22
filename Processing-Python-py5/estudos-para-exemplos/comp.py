pontos = []
for i in range(11):
    x = i * 10
    y = 50 + random(-25, 25)
    pontos.append((x, y))  # os parenteses extra criam uma tupla
    
no_fill()
with begin_shape():
    vertices(pontos)
save('random_poly.png')


    
# no_fill()
# with begin_shape():
#     vertices((i * 10, 50 + random(-25, 25))
#               for i in range(10))
