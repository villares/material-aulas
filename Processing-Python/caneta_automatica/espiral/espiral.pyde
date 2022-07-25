from caneta_automatica import *

size(400, 400)
inicie_caneta()

# sequencia = [1, 1, 2, 2, 3, 3, 4, 4] 

sequencia = []  # uma lista vazia
for n in range(1, 101):  # n de 1 a 100
    sequencia.append(n)
    sequencia.append(n) # joga pra dentro duas vezes o n...

for t in sequencia:
    ande(t * 4)  # 4 é o tamanho do passo
    vire(90)
    
