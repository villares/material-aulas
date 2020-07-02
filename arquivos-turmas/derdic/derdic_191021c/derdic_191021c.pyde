# lá em cimam fora do setup
py_alvo = 100 # onde o py vai chegar


# dentro do setup, mudar o global
    global px, py, tamanho_atual, cor_bola # aviso pra poder mudar os números
    # e por mais isto:
    py = py + (py_alvo - py) / 4
    
# lá no final do draw():
    global py_alvo # vou mudar o alvo!!!
    if key == "1": # tecla "1"
        py_alvo = 100
    if key == "4": # tecla "4"
        py_alvo = 400        
    if key == "1": # tecla "1"
        py_alvo = 100
    if key == " ": # tecla epaço
        py_alvo = 250  
        
